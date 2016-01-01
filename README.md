# SampleLWPCMSModule
## Structure & naming
> The name of the root directory of your LWPCMS module needs to end with _module<br>
> For example: SampleLWPCMSModule_module.

> The root directory of your LWPCMS plugin should always contain a __init__.py file,
> otherwise, Python won't recognize it as a package.
> LWPCMS modules/plugins are actually python packages, the only difference is the
> module.json file.<br>
> Here is a list of things your root directory needs to have:
> * \_\_init\_\_.py - Python wants it.
> * module.py - Containts your plugin class.
> * module.json - Contains meta about your plugin.

> For further information, please checkout the source code of this project.
