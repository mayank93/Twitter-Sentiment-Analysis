#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of web2py Web Framework (Copyrighted, 2007-2009).
Developed by Massimo Di Pierro <mdipierro@cs.depaul.edu>.
License: GPL v2

Tinkered by Szabolcs Gyuris < szimszo n @ o regpreshaz dot eu>
"""

class CasAuth( object ):
    """
    Login will be done via Web2py's CAS application, instead of web2py's
    login form.
    
    Include in your model (eg db.py)::
        
        from gluon.contrib.login_methods.cas_auth import CasAuth
        auth.settings.login_form=CasAuth()
        auth.settings.login_form.settings( globals(),
                 urlbase = "https://web2py.com/cas/cas" )

    where urlbase is the actual CAS server url without the login,logout...
    Enjoy.
    """
    def settings( self, g, urlbase = "https://login.iiit.ac.in/cas" ):
        self.urlbase=urlbase
        self.cas_login_url="%s/login"%self.urlbase
        self.cas_check_url="%s/validate"%self.urlbase
        self.cas_logout_url="%s/logout"%self.urlbase
        self.globals=g
        self.request=self.globals['request']
        self.session=self.globals['session']
        http_host='web2py.iiit.ac.in'
        self.cas_my_url='http://%s%s'%( http_host, self.request.env.path_info )
    def login_url( self, next = "/" ):
        self.session.token=self._CAS_login()
        return next
    def logout_url( self, next = "/" ):
        self.session.token=None
        self.session.auth=None
        self._CAS_logout()
        return next
    def get_user( self ):
        user=self.session.token
        if user:
            #return dict( email = user, source = "iiith cas" )
            return dict( email = user[0], source = "iiith cas" )
    def _CAS_login( self ):
        """
        exposed as CAS.login(request)
        returns a token on success, None on failed authentication
        """
        import urllib
        self.ticket=self.request.vars.ticket
        if not self.request.vars.ticket:
            self.globals['redirect']( "%s?service=%s"%( self.cas_login_url,
                                          self.cas_my_url ) )
        else:
            url="%s?service=%s&ticket=%s"%\
                                                           ( self.cas_check_url,
                                                            self.cas_my_url,
                                                            self.ticket )
            data=urllib.urlopen( url ).read().split( '\n' )
            if data[0]=='yes': return data[1].split( ':' )
        return None

    def _CAS_logout( self ):
        """
        exposed CAS.logout()
        redirects to the CAS logout page
        """
        import urllib
        self.globals['redirect']( "%s?service=%s"%( 
                                                  self.cas_logout_url,
                                                  self.cas_my_url ) )
