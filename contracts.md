# Portfolio Backend API Contracts

## Overview
This document defines the API contracts for Robert Chang's portfolio website backend integration.

## Current Mock Data to Replace
Located in `/app/frontend/src/data/mock.js`:
- Personal information and profile data
- Experience timeline data  
- Truffle expertise metrics and achievements
- Testimonials data
- Contact form submissions (currently frontend-only)

## Required Backend Models

### 1. Contact Submission Model
```javascript
ContactSubmission = {
  _id: ObjectId,
  name: String (required),
  email: String (required, validated),
  subject: String (required),
  message: String (required),
  inquiryType: String (enum: ['Business Partnership', 'Executive Opportunity', 'Truffle Collaboration', 'Consulting Services', 'Other']),
  submittedAt: Date (auto-generated),
  status: String (enum: ['new', 'read', 'responded'], default: 'new'),
  ipAddress: String (optional),
  userAgent: String (optional)
}
```

### 2. Profile Data Model (Static/Configurable)
```javascript
ProfileData = {
  _id: ObjectId,
  personal: {
    name: String,
    title: String,
    company: String,
    location: String,
    summary: String,
    languages: [String],
    specialties: [String]
  },
  updatedAt: Date
}
```

### 3. Experience Model
```javascript
Experience = {
  _id: ObjectId,
  company: String (required),
  position: String (required),
  duration: String (required),
  location: String,
  description: String (required),
  achievements: [String],
  order: Number (for sorting),
  isActive: Boolean (default: true)
}
```

### 4. Testimonial Model
```javascript
Testimonial = {
  _id: ObjectId,
  name: String (required),
  title: String (required),
  content: String (required),
  avatar: String (URL),
  isActive: Boolean (default: true),
  order: Number (for sorting)
}
```

## API Endpoints to Implement

### Contact Endpoints
- `POST /api/contact` - Submit contact form
- `GET /api/contact` - Get all submissions (admin only)
- `PATCH /api/contact/:id/status` - Update submission status

### Profile Data Endpoints  
- `GET /api/profile` - Get profile information
- `PUT /api/profile` - Update profile information (admin only)

### Experience Endpoints
- `GET /api/experience` - Get all experience entries
- `POST /api/experience` - Add new experience (admin only)
- `PUT /api/experience/:id` - Update experience (admin only)
- `DELETE /api/experience/:id` - Delete experience (admin only)

### Testimonial Endpoints
- `GET /api/testimonials` - Get all active testimonials
- `POST /api/testimonials` - Add new testimonial (admin only)
- `PUT /api/testimonials/:id` - Update testimonial (admin only)
- `DELETE /api/testimonials/:id` - Delete testimonial (admin only)

### Truffle Expertise Endpoints
- `GET /api/expertise` - Get truffle expertise data
- `PUT /api/expertise` - Update expertise data (admin only)

## Frontend Integration Plan

### 1. Contact Form Integration
Replace mock form submission in `ContactSection.jsx`:
- Remove setTimeout simulation
- Add actual API call to `POST /api/contact`
- Handle real success/error responses
- Implement proper error handling and validation

### 2. Data Fetching Integration
Replace static mock imports with API calls in:
- `App.js` - Fetch profile, experience, testimonials, expertise data
- Add loading states for better UX
- Implement error handling for API failures

### 3. Environment Variables
Use existing `REACT_APP_BACKEND_URL` from frontend `.env` for all API calls.

## Response Formats

### Success Response
```javascript
{
  "success": true,
  "data": {}, // Response data
  "message": "Operation completed successfully"
}
```

### Error Response  
```javascript
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human readable error message",
    "details": {} // Optional additional details
  }
}
```

## Validation Rules

### Contact Form Validation
- `name`: 2-100 characters, required
- `email`: Valid email format, required
- `subject`: 5-200 characters, required  
- `message`: 10-2000 characters, required
- `inquiryType`: Must be one of allowed enum values

### Rate Limiting
- Contact submissions: 3 per hour per IP address
- General API calls: 100 per hour per IP address

## Security Considerations
- Email validation and sanitization
- XSS prevention in all text inputs
- Rate limiting on contact submissions
- Input validation and sanitization
- CORS properly configured

## Integration Steps
1. Implement MongoDB models and validation
2. Create API endpoints with proper error handling
3. Test backend endpoints independently
4. Update frontend to use real API calls
5. Remove mock data dependencies
6. Test full integration
7. Handle edge cases and error states