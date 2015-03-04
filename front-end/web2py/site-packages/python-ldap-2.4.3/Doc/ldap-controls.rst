.. % $Id: ldap-controls.rst,v 1.10 2011/07/23 08:15:38 stroeder Exp $


<<<<<<< ldap-controls.rst
:py:mod:`ldap.controls` High-level access to LDAPv3 extended controls
=====================================================================
=======
*********************************************************************
:py:mod:`ldap.controls` High-level access to LDAPv3 extended controls
*********************************************************************
>>>>>>> 1.6

.. py:module:: ldap.controls
   :synopsis: High-level access to LDAPv3 extended controls.
.. moduleauthor:: python-ldap project (see http://www.python-ldap.org/)


Variables
=========

.. py:data:: KNOWN_RESPONSE_CONTROLS

   Dictionary mapping the OIDs of known response controls to the accompanying
   :py:class:`ResponseControl` classes. This is used
   by :py:func:`DecodeControlTuples` to automatically decode control values.
   Calling application can also register their custom :py:class:`ResponseControl`
   classes in this dictionary possibly overriding pre-registered classes.


Classes
=======

This module defines the following classes:

<<<<<<< ldap-controls.rst
.. py:class:: LDAPControl(controlType, criticality [, controlValue=:const:`None` [, encodedControlValue=:const:`None`]])
=======

.. autoclass:: ldap.controls.RequestControl
   :members:
>>>>>>> 1.6

.. autoclass:: ldap.controls.ResponseControl
   :members:

.. autoclass:: ldap.controls.LDAPControl
   :members:

<<<<<<< ldap-controls.rst
   .. py:method:: LDAPControl.encodeControlValue(value)
=======
>>>>>>> 1.6

Functions
=========

This module defines the following functions:

<<<<<<< ldap-controls.rst
   .. py:method:: LDAPControl.decodeControlValue(value)
=======
>>>>>>> 1.6

.. autofunction:: ldap.controls.RequestControlTuples

.. autofunction:: ldap.controls.DecodeControlTuples

<<<<<<< ldap-controls.rst
   .. py:method:: LDAPControl.getEncodedTuple()
=======
>>>>>>> 1.6

<<<<<<< ldap-controls.rst
      Return a readily encoded 3-tuple which can be directly  passed to C module
      :py:mod:_ldap. This method is called by  function :py:func:`ldap.EncodeControlTuples`.
=======
Sub-modules
===========
>>>>>>> 1.6

Various sub-modules implement specific LDAPv3 extended controls. The classes
therein are derived from the base-classes :py:class:`ldap.controls.RequestControl`,
:py:class:`ldap.controls.ResponseControl` or :py:class:`ldap.controls.LDAPControl`.

<<<<<<< ldap-controls.rst
<<<<<<< ldap-controls.rst
.. py:class:: BooleanControl(controlType, criticality [, controlValue=:const:`None` [, encodedControlValue=:const:`None`]])
=======
Some of them require :py:mod:`pyasn1` and :py:mod:`pyasn1_modules` to be installed.
>>>>>>> 1.6
=======
Some of them require :py:mod:`pyasn1` and :py:mod:`pyasn1_modules` to be installed:

Usually the names of the method arguments and the class attributes match
the ASN.1 identifiers used in the specification. So looking at the referenced
RFC or Internet-Draft is very helpful to understand the API.
>>>>>>> 1.10


:py:mod:`ldap.controls.simple` Very simple controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:module:: ldap.controls.simple
   :synopsis: simple request and response controls implemented in pure Python


.. autoclass:: ldap.controls.simple.ValueLessRequestControl
   :members:

.. autoclass:: ldap.controls.simple.OctetStringInteger
   :members:

.. autoclass:: ldap.controls.simple.BooleanControl
   :members:

<<<<<<< ldap-controls.rst
<<<<<<< ldap-controls.rst

.. py:class:: SimplePagedResultsControl(controlType, criticality [, controlValue=:const:`None` [, encodedControlValue=:const:`None`]])
=======
.. automodule:: ldap.controls.simple
=======
.. autoclass:: ldap.controls.simple.ManageDSAITControl
>>>>>>> 1.10
   :members:
>>>>>>> 1.6

   .. seealso::

      :rfc:`3296` - Named Subordinate References in Lightweight Directory Access Protocol (LDAP) Directories

.. autoclass:: ldap.controls.simple.RelaxRulesControl
   :members:

   .. seealso::

      http://tools.ietf.org/draft/draft-zeilenga-ldap-relax/

.. autoclass:: ldap.controls.simple.ProxyAuthzControl
   :members:

   .. seealso::

      :rfc:`4370` - Lightweight Directory Access Protocol (LDAP): Proxied Authorization Control

.. autoclass:: ldap.controls.simple.AuthorizationIdentityControl
   :members:

   .. seealso::

      :rfc:`3829` - Lightweight Directory Access Protocol (LDAP): Authorization Identity Request and Response Controls

.. autoclass:: ldap.controls.simple.GetEffectiveRightsControl
   :members:


<<<<<<< ldap-controls.rst
<<<<<<< ldap-controls.rst

.. py:class:: MatchedValuesControl(criticality [, controlValue=:const:`None`])
=======
=======

>>>>>>> 1.10
:py:mod:`ldap.controls.libldap` Various controls implemented in OpenLDAP libs
<<<<<<< ldap-controls.rst
=============================================================================
>>>>>>> 1.6
=======
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>>>>>> 1.10

.. py:module:: ldap.controls.libldap
   :synopsis: request and response controls implemented by OpenLDAP libs

<<<<<<< ldap-controls.rst
   .. seealso::
=======
This module wraps C functions in OpenLDAP client libs which implement various
request and response controls into Python classes.

>>>>>>> 1.6

.. autoclass:: ldap.controls.libldap.AssertionControl
   :members:

<<<<<<< ldap-controls.rst
<<<<<<< ldap-controls.rst
=======
.. seealso::
>>>>>>> 1.6
=======
   .. seealso::
>>>>>>> 1.10

<<<<<<< ldap-controls.rst
<<<<<<< ldap-controls.rst
Functions
=========
=======
   :rfc:`4528` - Lightweight Directory Access Protocol (LDAP) Assertion Control
>>>>>>> 1.6
=======
      :rfc:`4528` - Lightweight Directory Access Protocol (LDAP) Assertion Control
>>>>>>> 1.10

<<<<<<< ldap-controls.rst
This module defines the following functions:

.. py:function:: EncodeControlTuples(ldapControls) -> list
=======
>>>>>>> 1.6

.. autoclass:: ldap.controls.libldap.MatchedValuesControl
   :members:

<<<<<<< ldap-controls.rst
<<<<<<< ldap-controls.rst
=======
.. seealso::
=======
   .. seealso::
>>>>>>> 1.10

<<<<<<< ldap-controls.rst
   :rfc:`3876` - Returning Matched Values with the Lightweight Directory Access Protocol version 3 (LDAPv3)
>>>>>>> 1.6
=======
      :rfc:`3876` - Returning Matched Values with the Lightweight Directory Access Protocol version 3 (LDAPv3)
>>>>>>> 1.10

<<<<<<< ldap-controls.rst
.. py:function:: DecodeControlTuples(ldapControlTuples) -> list
=======
>>>>>>> 1.6

.. autoclass:: ldap.controls.libldap.SimplePagedResultsControl
   :members:

<<<<<<< ldap-controls.rst
<<<<<<< ldap-controls.rst
=======
.. seealso::
=======
   .. seealso::
>>>>>>> 1.10

      :rfc:`2696` - LDAP Control Extension for Simple Paged Results Manipulation


:py:mod:`ldap.controls.psearch` LDAP Persistent Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:module:: ldap.controls.psearch
   :synopsis: request and response controls for LDAP persistent search

This module implements request and response controls for LDAP persistent
search.

.. seealso::

   http://tools.ietf.org/html/draft-ietf-ldapext-psearch


.. autoclass:: ldap.controls.psearch.PersistentSearchControl
   :members:

.. autoclass:: ldap.controls.psearch.EntryChangeNotificationControl
   :members:

<<<<<<< ldap-controls.rst
>>>>>>> 1.6
=======

:py:mod:`ldap.controls.sessiontrack` Session tracking control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:module:: ldap.controls.sessiontrack
   :synopsis: request control for session tracking

.. seealso::

   http://tools.ietf.org/html/draft-wahl-ldap-session


.. autoclass:: ldap.controls.sessiontrack.SessionTrackingControl
   :members:


:py:mod:`ldap.controls.readentry` Read entry control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:module:: ldap.controls.readentry
   :synopsis: read entryrequest and response controls

.. seealso::

   :rfc:`4527` - Lightweight Directory Access Protocol (LDAP): Read Entry Controls


.. autoclass:: ldap.controls.readentry.ReadEntryControl
   :members:

.. autoclass:: ldap.controls.readentry.PreReadControl
   :members:

.. autoclass:: ldap.controls.readentry.PostReadControl
   :members:
>>>>>>> 1.10
