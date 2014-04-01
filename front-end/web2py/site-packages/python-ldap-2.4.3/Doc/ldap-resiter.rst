.. % $Id: ldap-resiter.rst,v 1.3 2011/07/21 20:33:26 stroeder Exp $


:py:mod:`ldap.resiter` Generator for stream-processing of large search results
==============================================================================

.. py:module:: ldap.resiter
   :synopsis: Generator for stream-processing of large search results.
.. moduleauthor:: python-ldap project (see http://www.python-ldap.org/)


.. % Author of the module code;


.. _ldap.resiter-example:

Examples for ldap.resiter
-------------------------

.. _ldap.resiter.ResultProcessor-example:

Using ldap.resiter
^^^^^^^^^^^^^^^^^^

This example demonstrates how to use mix-in class ldap.resiter.ResultProcessor for
retrieving results and processing them in a for-loop. ::

  import sys,ldap,ldap.resiter

  class MyLDAPObject(ldap.ldapobject.LDAPObject,ldap.resiter.ResultProcessor):
    pass

  l = MyLDAPObject('ldap://localhost')

  # Asynchronous search method
  msg_id = l.search('dc=stroeder,dc=com',ldap.SCOPE_SUBTREE,'(objectClass=*)')

  for res_type,res_data,res_msgid,res_controls in self.source.allresults(msg_id):
    for dn,entry in res_data:
      # process dn and entry
      print dn,entry['objectClass']
