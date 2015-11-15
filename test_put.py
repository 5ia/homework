import requests
import unittest


class TestUpdate(unittest.TestCase):
    
    VALID_USR='myself'
    VALID_PASS='mypass'
    APP_NAME='MyApp'
    DOMAIN="https://my.domain.com"
    APPID = '123'
    PERMISSIONS = [ "A", "C" ] #WHAT ARE THE VALID PERMISSIONS? ARE THERE INVALID ONES AS WELL?
    INV_USR='john' #user that is not registered
    INV_PASS='random'
    USR2='ben'
    PSW2='benspass'
    APP_NEW_NAME='MyNewApp'
    NEW_DOMAIN="https://my.newdomain.com"
    INV_APPID="8979" # there should be no app with this ID
    
    def test_valid_auth_data(self):
        """ Test with correct authentication and valid data"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code, 200)
        
    def test_missing_auth(self):
        """ Test request without any authentication"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata)
        self.assertEqual(r.status_code,403)
        
    def test_missing_usr(self):
        """ Test request without user value passed in auth"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=('', self.VALID_PASS))
        self.assertEqual(r.status_code,403)
        
    def test_missing_pass(self):
        """ Test request without password value passed in auth"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, ''))
        self.assertEqual(r.status_code,403)
        
    def test_wrong_usr(self):
        """ Test request with unexisting user value passed in auth"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.INV_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,403)
        
    def test_wrong_pass(self):
        """ Test request with incorrect password value passed in auth"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.INV_PASS))
        self.assertEqual(r.status_code,403)
        
    def test_wrong_owner(self):
        """ Test request with user that is not the owner of the app"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.USR2, self.PSW2))
        self.assertEqual(r.status_code,403)
        
    def test_name_update(self):
        """ Test request trying to update application name"""
        mydata = {"name" : self.APP_NEW_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,403)
        
    def test_domain_update(self):
        """ Test request trying to update domain name"""
        mydata = {"name" : self.APP_NAME, "domain" : self.NEW_DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,403)
        
    def test_missing_body(self):
        """ Test request without a body"""
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,400)
        
    def test_missing_appname(self):
        """ Test request without app name"""
        mydata = { "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.APP_NAME))
        self.assertEqual(r.status_code,400)
        
    def test_missing_domain(self):
        """ Test request without a domain"""
        mydata = {"name" : self.APP_NAME, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,400)
        
    def test_missing_perms(self):
        """ Test request without permissions part"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,400)
        
    def test_unknown_element(self):
        """ Test request with additional part in body that is not defined in specs"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS, "new_option": "myoption"}
        url = self.DOMAIN + '/apps/' + self.APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,400)
        
    def test_missing_appid(self):
        """ Test request without application Id"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' 
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,500)
        
    def test_missing_app(self):
        """ Test request for non-existant application"""
        mydata = {"name" : self.APP_NAME, "domain" : self.DOMAIN, "permissions" : self.PERMISSIONS}
        url = self.DOMAIN + '/apps/' + self.INV_APPID
        r=requests.put(url,data=mydata, auth=(self.VALID_USR, self.VALID_PASS))
        self.assertEqual(r.status_code,404)
        


if __name__ == '__main__':
    unittest.main()
