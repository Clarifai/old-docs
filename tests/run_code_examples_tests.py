import os


def read_init_code():
  init_lines = []

  with open("../api-guide/api-overview/api-clients/README.md") as f:
    in_install_instructions = False
    in_python_initialize_client = False
    for line in f:
      line = line[:-1]  # Remove ending newline char
      if in_python_initialize_client:
        if line == "```":
          break
        init_lines.append(line)
      elif in_install_instructions:
        if line.startswith("# Initialize client"):
          in_python_initialize_client = True
      elif line.startswith("## Client Installation Instructions"):
        in_install_instructions = True


  init_script = "\n".join(init_lines)
  init_script += "\n\n"
  return init_script


def read_code_examples(file_path):
  code_lines = []
  with open("../api-guide/" + file_path) as f:
    num = 1
    in_python_code = False
    title = ""
    for line in f:
      line = line[:-1]  # Remove ending newline char
      if in_python_code:
        if line == "```":
          in_python_code = False
          code_lines.append("\n\n")
        else:
          code_lines.append(line)
      elif line == "```python":
        in_python_code = True
        code_lines.append("#")
        code_lines.append(f"# Code example ({num}): {title}")
        code_lines.append("#")
        num += 1
      elif line.startswith("## "):
        title = line[len("## "):]
  return "\n".join(code_lines)


def make_test_setup_code(code_examples):
  """
  Extends the documentation code examples with code that needs to be run in
  order for tests to succeed.

  For example, before each PostApps, we add a DeleteApp of that app_id,
  to delete any possible previous existing app.
  """
  creates_app = False
  app_id = ""
  for line in code_examples.split("\n"):
    if "stub.PostApps" in line:
      creates_app = True
    elif creates_app and not app_id and "id=" in line:
      app_id = line.strip()[len('id="'):-len(",)")]

  code_examples = ""
  if app_id:
    code_examples = """
# This is not part of the docs. It is added to the test run, to clean up
# any possible app with this name from any previous (failed) test runs.
stub.DeleteApp(
    service_pb2.DeleteAppRequest(
        user_app_id=resources_pb2.UserAppIDSet(user_id="me", app_id="%s")
    ),
    metadata=(('authorization', 'Key %s'),)
)

""" % (app_id, PAT)

  return code_examples


if __name__ == "__main__":
  PAT = os.environ["TEST_RUNNER_PAT"]

  file_paths = [
    # TODO: App/key creation needs to be added to this test code runner.
    # "walkthroughs/custom-text-model-walkthrough.md"
  ]

  init_code = read_init_code()
  for file_path in file_paths:
    code_examples = read_code_examples(file_path)

    test_setup_code = make_test_setup_code(code_examples)

    total_code = init_code + test_setup_code + code_examples
    total_code = total_code.replace("{YOUR_PERSONAL_ACCESS_TOKEN}", PAT)

    print("### Testing code examples in " + file_path)
    print("### The following code will be run:")
    print()

    for i, line in enumerate(total_code.split("\n")):
      print(f"{i + 1:5d} | {line}")

    print()
    print("### Running the code, standard output:")
    exec(total_code)
