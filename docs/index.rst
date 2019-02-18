.. e-invite documentation master file, created by
   sphinx-quickstart on Sat Feb 16 13:31:12 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

E-invite project documentation
==============================

E-invite is a web app to create electronic invitations in video file format which is downloadable and share able 
over internet.

* To create video invitation user must signed in.
* User can create multiple invitation card and download them.

.. code-block:: python

	pip install django

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

       
.. toctree::
   :maxdepth: 2
   :caption: Project Packages
   :hidden:

   _modules/e_invite
   _modules/invi_cards
   _modules/dashboard


