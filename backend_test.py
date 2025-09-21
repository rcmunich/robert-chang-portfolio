#!/usr/bin/env python3
"""
Backend API Test Suite for Robert Chang's Portfolio Website
Tests all API endpoints including validation, rate limiting, and error handling
"""

import requests
import json
import time
import os
from datetime import datetime
from typing import Dict, Any

# Get backend URL from environment
BACKEND_URL = "https://truffle-leader.preview.emergentagent.com"
API_BASE = f"{BACKEND_URL}/api"

class PortfolioAPITester:
    def __init__(self):
        self.session = requests.Session()
        self.test_results = []
        
    def log_test(self, test_name: str, success: bool, details: str = ""):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   Details: {details}")
        
        self.test_results.append({
            "test": test_name,
            "success": success,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })
    
    def test_health_check(self):
        """Test health check endpoint"""
        try:
            response = self.session.get(f"{BACKEND_URL}/health", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy" and data.get("service") == "portfolio-api":
                    self.log_test("Health Check", True, f"Status: {data}")
                    return True
                else:
                    self.log_test("Health Check", False, f"Unexpected response: {data}")
                    return False
            else:
                self.log_test("Health Check", False, f"Status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_test("Health Check", False, f"Exception: {str(e)}")
            return False
    
    def test_contact_form_valid(self):
        """Test contact form with valid data"""
        try:
            valid_data = {
                "name": "John Smith",
                "email": "john.smith@example.com",
                "subject": "Business Partnership Inquiry",
                "message": "I am interested in discussing potential business partnership opportunities with American Truffle Company. Could we schedule a call?",
                "inquiryType": "Business Partnership"
            }
            
            response = self.session.post(
                f"{API_BASE}/contact",
                json=valid_data,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success") and "id" in data.get("data", {}):
                    self.log_test("Contact Form - Valid Data", True, f"Submission ID: {data['data']['id']}")
                    return True
                else:
                    self.log_test("Contact Form - Valid Data", False, f"Unexpected response: {data}")
                    return False
            else:
                self.log_test("Contact Form - Valid Data", False, f"Status code: {response.status_code}, Response: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Contact Form - Valid Data", False, f"Exception: {str(e)}")
            return False
    
    def test_contact_form_inquiry_types(self):
        """Test contact form with different inquiry types"""
        inquiry_types = [
            "Business Partnership",
            "Executive Opportunity", 
            "Truffle Collaboration",
            "Consulting Services",
            "Other"
        ]
        
        success_count = 0
        for inquiry_type in inquiry_types:
            try:
                data = {
                    "name": f"Test User {inquiry_type}",
                    "email": f"test.{inquiry_type.lower().replace(' ', '.')}@example.com",
                    "subject": f"Test {inquiry_type} Inquiry",
                    "message": f"This is a test message for {inquiry_type} inquiry type. Testing the API endpoint functionality.",
                    "inquiryType": inquiry_type
                }
                
                response = self.session.post(
                    f"{API_BASE}/contact",
                    json=data,
                    timeout=10
                )
                
                if response.status_code == 200:
                    response_data = response.json()
                    if response_data.get("success"):
                        success_count += 1
                    else:
                        self.log_test(f"Contact Form - {inquiry_type}", False, f"Response: {response_data}")
                else:
                    self.log_test(f"Contact Form - {inquiry_type}", False, f"Status: {response.status_code}")
                    
            except Exception as e:
                self.log_test(f"Contact Form - {inquiry_type}", False, f"Exception: {str(e)}")
        
        if success_count == len(inquiry_types):
            self.log_test("Contact Form - All Inquiry Types", True, f"All {len(inquiry_types)} inquiry types accepted")
            return True
        else:
            self.log_test("Contact Form - All Inquiry Types", False, f"Only {success_count}/{len(inquiry_types)} inquiry types worked")
            return False
    
    def test_contact_form_validation(self):
        """Test contact form validation"""
        test_cases = [
            {
                "name": "Missing Name",
                "data": {
                    "email": "test@example.com",
                    "subject": "Test Subject",
                    "message": "Test message content",
                    "inquiryType": "Other"
                },
                "should_fail": True
            },
            {
                "name": "Invalid Email",
                "data": {
                    "name": "Test User",
                    "email": "invalid-email",
                    "subject": "Test Subject", 
                    "message": "Test message content",
                    "inquiryType": "Other"
                },
                "should_fail": True
            },
            {
                "name": "Short Subject",
                "data": {
                    "name": "Test User",
                    "email": "test@example.com",
                    "subject": "Hi",
                    "message": "Test message content",
                    "inquiryType": "Other"
                },
                "should_fail": True
            },
            {
                "name": "Short Message",
                "data": {
                    "name": "Test User",
                    "email": "test@example.com",
                    "subject": "Test Subject",
                    "message": "Short",
                    "inquiryType": "Other"
                },
                "should_fail": True
            }
        ]
        
        validation_passed = 0
        for test_case in test_cases:
            try:
                response = self.session.post(
                    f"{API_BASE}/contact",
                    json=test_case["data"],
                    timeout=10
                )
                
                if test_case["should_fail"]:
                    if response.status_code >= 400:
                        validation_passed += 1
                        self.log_test(f"Validation - {test_case['name']}", True, "Correctly rejected invalid data")
                    else:
                        self.log_test(f"Validation - {test_case['name']}", False, "Should have been rejected but was accepted")
                else:
                    if response.status_code == 200:
                        validation_passed += 1
                        self.log_test(f"Validation - {test_case['name']}", True, "Correctly accepted valid data")
                    else:
                        self.log_test(f"Validation - {test_case['name']}", False, "Should have been accepted but was rejected")
                        
            except Exception as e:
                self.log_test(f"Validation - {test_case['name']}", False, f"Exception: {str(e)}")
        
        return validation_passed == len(test_cases)
    
    def test_rate_limiting(self):
        """Test rate limiting (max 3 requests per hour per IP)"""
        try:
            # Make 4 requests quickly to test rate limiting
            responses = []
            for i in range(4):
                data = {
                    "name": f"Rate Test User {i}",
                    "email": f"ratetest{i}@example.com",
                    "subject": f"Rate Limit Test {i}",
                    "message": "This is a test message for rate limiting functionality.",
                    "inquiryType": "Other"
                }
                
                response = self.session.post(
                    f"{API_BASE}/contact",
                    json=data,
                    timeout=10
                )
                responses.append(response)
                time.sleep(0.1)  # Small delay between requests
            
            # First 3 should succeed, 4th should be rate limited
            success_count = sum(1 for r in responses[:3] if r.status_code == 200)
            rate_limited = responses[3].status_code == 429
            
            if success_count == 3 and rate_limited:
                self.log_test("Rate Limiting", True, "First 3 requests succeeded, 4th was rate limited")
                return True
            else:
                self.log_test("Rate Limiting", False, f"Success count: {success_count}, Rate limited: {rate_limited}")
                return False
                
        except Exception as e:
            self.log_test("Rate Limiting", False, f"Exception: {str(e)}")
            return False
    
    def test_profile_endpoint(self):
        """Test profile data endpoint"""
        try:
            response = self.session.get(f"{API_BASE}/profile", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success") and "data" in data:
                    profile_data = data["data"]
                    personal = profile_data.get("personal", {})
                    
                    # Check required fields
                    required_fields = ["name", "title", "company", "location", "summary", "languages", "specialties"]
                    missing_fields = [field for field in required_fields if field not in personal]
                    
                    if not missing_fields:
                        self.log_test("Profile Endpoint", True, f"All required fields present: {list(personal.keys())}")
                        return True
                    else:
                        self.log_test("Profile Endpoint", False, f"Missing fields: {missing_fields}")
                        return False
                else:
                    self.log_test("Profile Endpoint", False, f"Unexpected response structure: {data}")
                    return False
            else:
                self.log_test("Profile Endpoint", False, f"Status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_test("Profile Endpoint", False, f"Exception: {str(e)}")
            return False
    
    def test_experience_endpoint(self):
        """Test experience data endpoint"""
        try:
            response = self.session.get(f"{API_BASE}/experience", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success") and "data" in data:
                    experiences = data["data"]
                    
                    if isinstance(experiences, list) and len(experiences) > 0:
                        # Check first experience has required fields
                        first_exp = experiences[0]
                        required_fields = ["company", "position", "duration", "description", "achievements"]
                        missing_fields = [field for field in required_fields if field not in first_exp]
                        
                        if not missing_fields:
                            self.log_test("Experience Endpoint", True, f"Found {len(experiences)} experiences with required fields")
                            return True
                        else:
                            self.log_test("Experience Endpoint", False, f"Missing fields in experience: {missing_fields}")
                            return False
                    else:
                        self.log_test("Experience Endpoint", False, "No experiences found or invalid format")
                        return False
                else:
                    self.log_test("Experience Endpoint", False, f"Unexpected response structure: {data}")
                    return False
            else:
                self.log_test("Experience Endpoint", False, f"Status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_test("Experience Endpoint", False, f"Exception: {str(e)}")
            return False
    
    def test_testimonials_endpoint(self):
        """Test testimonials data endpoint"""
        try:
            response = self.session.get(f"{API_BASE}/testimonials", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success") and "data" in data:
                    testimonials = data["data"]
                    
                    if isinstance(testimonials, list) and len(testimonials) > 0:
                        # Check first testimonial has required fields
                        first_testimonial = testimonials[0]
                        required_fields = ["name", "title", "content"]
                        missing_fields = [field for field in required_fields if field not in first_testimonial]
                        
                        if not missing_fields:
                            self.log_test("Testimonials Endpoint", True, f"Found {len(testimonials)} testimonials with required fields")
                            return True
                        else:
                            self.log_test("Testimonials Endpoint", False, f"Missing fields in testimonial: {missing_fields}")
                            return False
                    else:
                        self.log_test("Testimonials Endpoint", False, "No testimonials found or invalid format")
                        return False
                else:
                    self.log_test("Testimonials Endpoint", False, f"Unexpected response structure: {data}")
                    return False
            else:
                self.log_test("Testimonials Endpoint", False, f"Status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_test("Testimonials Endpoint", False, f"Exception: {str(e)}")
            return False
    
    def test_expertise_endpoint(self):
        """Test truffle expertise data endpoint"""
        try:
            response = self.session.get(f"{API_BASE}/expertise", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success") and "data" in data:
                    expertise = data["data"]
                    
                    # Check required fields
                    required_fields = ["title", "subtitle", "description", "achievements", "metrics"]
                    missing_fields = [field for field in required_fields if field not in expertise]
                    
                    if not missing_fields:
                        # Check metrics structure
                        metrics = expertise.get("metrics", [])
                        if isinstance(metrics, list) and len(metrics) > 0:
                            first_metric = metrics[0]
                            if "label" in first_metric and "value" in first_metric:
                                self.log_test("Expertise Endpoint", True, f"All required fields present with {len(metrics)} metrics")
                                return True
                            else:
                                self.log_test("Expertise Endpoint", False, "Metrics missing label/value fields")
                                return False
                        else:
                            self.log_test("Expertise Endpoint", False, "No metrics found")
                            return False
                    else:
                        self.log_test("Expertise Endpoint", False, f"Missing fields: {missing_fields}")
                        return False
                else:
                    self.log_test("Expertise Endpoint", False, f"Unexpected response structure: {data}")
                    return False
            else:
                self.log_test("Expertise Endpoint", False, f"Status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_test("Expertise Endpoint", False, f"Exception: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all API tests"""
        print("=" * 60)
        print("ROBERT CHANG PORTFOLIO API TEST SUITE")
        print("=" * 60)
        print(f"Testing backend at: {BACKEND_URL}")
        print(f"API base URL: {API_BASE}")
        print("-" * 60)
        
        # Run all tests
        tests = [
            self.test_health_check,
            self.test_contact_form_valid,
            self.test_contact_form_inquiry_types,
            self.test_contact_form_validation,
            self.test_rate_limiting,
            self.test_profile_endpoint,
            self.test_experience_endpoint,
            self.test_testimonials_endpoint,
            self.test_expertise_endpoint
        ]
        
        passed = 0
        total = len(tests)
        
        for test in tests:
            try:
                if test():
                    passed += 1
            except Exception as e:
                print(f"❌ FAIL {test.__name__}: Unexpected error: {str(e)}")
        
        print("-" * 60)
        print(f"RESULTS: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 ALL TESTS PASSED!")
            return True
        else:
            print(f"⚠️  {total - passed} tests failed")
            return False

def main():
    """Main test execution"""
    tester = PortfolioAPITester()
    success = tester.run_all_tests()
    
    # Save detailed results
    with open('/app/backend_test_results.json', 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "backend_url": BACKEND_URL,
            "total_tests": len(tester.test_results),
            "passed_tests": sum(1 for r in tester.test_results if r["success"]),
            "overall_success": success,
            "detailed_results": tester.test_results
        }, f, indent=2)
    
    return success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)