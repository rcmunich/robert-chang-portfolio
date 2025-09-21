# Robert Chang - Professional Portfolio

A sophisticated full-stack portfolio website showcasing executive leadership in technology and truffle cultivation.

## 🌟 Features

- **Executive Profile**: Comprehensive professional summary
- **Experience Timeline**: 17+ years of global leadership positions
- **Truffle Innovation**: Unique agricultural expertise and achievements
- **Professional Testimonials**: Industry leader endorsements
- **Contact System**: Fully functional contact form with backend processing
- **Multilingual**: English, German, Mandarin Chinese, Japanese, Spanish

## 🚀 Tech Stack

### Frontend
- React 19
- Tailwind CSS
- Shadcn/UI Components
- Responsive Design

### Backend
- FastAPI (Python)
- MongoDB
- Pydantic Models
- RESTful API

## 📦 Deployment

### Railway Deployment

This project is configured for Railway deployment with both frontend and backend.

#### Environment Variables Needed:
```
MONGO_URL=your_mongodb_connection_string
DB_NAME=portfolio_db
REACT_APP_BACKEND_URL=your_backend_url
```

#### Deploy Steps:
1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push to main branch

### Local Development

#### Backend Setup:
```bash
cd backend
pip install -r requirements.txt
uvicorn server:app --reload --port 8001
```

#### Frontend Setup:
```bash
cd frontend
yarn install
yarn start
```

## 🎯 Contact Form Features

- Real-time validation
- Multiple inquiry types
- Rate limiting (3 submissions/hour)
- Professional response system
- Error handling

## 🔧 API Endpoints

- `GET /api/profile` - Profile information
- `GET /api/experience` - Career timeline
- `GET /api/testimonials` - Professional references
- `GET /api/expertise` - Truffle cultivation expertise
- `POST /api/contact` - Contact form submission
- `GET /health` - Health check

## 📱 Responsive Design

Optimized for all devices:
- Desktop (1920px+)
- Tablet (768px - 1199px)
- Mobile (< 768px)

## 🎨 Design System

- **Colors**: Sophisticated slate backgrounds with amber accents
- **Typography**: Professional hierarchy with clean fonts
- **Animations**: Subtle micro-interactions and smooth transitions
- **Components**: Modern shadcn/ui component library

## 📈 Performance

- Fast loading with optimized images
- Efficient API calls
- Responsive layouts
- SEO-friendly structure

---

**Built for Robert Chang** - Managing Director & Chief Truffle Officer, American Truffle Company
