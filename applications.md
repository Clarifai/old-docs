### Applications

API calls are tied to an account and application. Any model you create or search indexes you add images to,
will be contained within an application.

You can create as many applications as you want and can edit or delete them as you see fit. Each application
has a unique API Key. These are used for authentication. You can
[learn more about authentication](authentication.md) above.

#### Create an Application

To create an application, head on over to the [applications page](https://portal.clarifai.com/apps)
and press the 'Create a New Application' button.

At a minimum, you'll need to provide an application name and a public model to choose as your Base Workflow. You
may also set the [default language](languages.md#default-language). If you plan on using a language other than English, you must use
the General model. You can learn more about models and languages in the
[public model guide](public-models.md) above.

![image showing the edit app button on the Manage Application page](/images/create-new-app-new.png)

#### Base Workflow

When you create an application, you will need to select a Base Workflow, along with App Name and Default Language. You can choose from a select list of public models as your Base Workflow.

The Base Workflow you choose will optimize custom trained models to use the knowledge base from the selected public model. For example, if you're training a custom model around food, you could choose the Food model to gain optimized results. We recommend choosing the General model if you're not sure which public model would best suit your inputs.

Check out our [model gallery](https://www.clarifai.com/models) for a description of the select public models that can be used as a base workflow. Also note that you cannot change the Base Workflow of an app once it's created.

#### Edit an Application

If at any point you'd like to change the application name, add/remove API Keys, and modify Workflow management for Predict, you may do so by visiting the application page and changing the values.

![Image showing the edit application screen where you can change the name, add api keys, or delete the application](/images/edit-app-new.png)

#### Delete an Application

If you'd like to delete an application, you may do so at any time by visiting the application page and
pressing the 'Delete application' button. You'll be asked to confirm your change. Please note that once you
delete an application, we cannot recover it. You will also lose all images, concepts and models associated
with that application. **Proceed with caution**.
