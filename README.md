# AutomatedTesting_SeleniumPython

This project is a suite of tests made for an eCommerce site, created with WordPress.

See here the worpress site files: [Esite_wordpress_site_files](https://drive.google.com/file/d/1k9a5gT1_UjquY3-opfxDbe_LZlQbmw88/view?usp=sharing)

For site configurantion and running tests see: Site configuration and run tests.pdf
Site description:

-A basic site with the WooCommerce plugin and Dokan plugin (multi-vendor).
-It is a site made for testing purposes only.

Site documentation:
- You can find the UI documentation in the document: Esite - documentation.pdf.

Test plan:
- See the document dedicated to it, including test cases and steps.
- ‼ More test scenarios can be seen in the dedicated file (Test Plan Esite - TC). Tests without steps don't have scripts.

Test scripts:

- There are test scripts for the following scenarios:
**Login and registration positive and negative flows
**End-to-end flow: placing order as guest and making an account after placing first order
**Cart content verification (coupon application)
‼ You can find the scripts in the folder WordPress_EcommerceSite_Tested_With_Selenium_Python.


!!Please see recorded video with tests run and test reports here + screenshot of tests reports: [Google Drive link to video and SS](https://drive.google.com/drive/folders/1JWQ9gRWdNafi-goXiRRfs6jSi8zCJ9OU?usp=drive_link)

Helpers used to run tests:

--To set up the environment.
--To set up the DB connection.
--To disable prompts (later updated the init_driver function to handle this).
--To complete forms with random data using the Faker library.
--To generate random emails and passwords using the Random library.

