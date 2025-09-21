import React, { useState, useEffect } from "react";
import "./App.css";
import Header from "./components/Header";
import HeroSection from "./components/HeroSection";
import ExperienceSection from "./components/ExperienceSection";
import TruffleExpertiseSection from "./components/TruffleExpertiseSection";
import TestimonialsSection from "./components/TestimonialsSection";
import ContactSection from "./components/ContactSection";
import Footer from "./components/Footer";
import { Toaster } from "./components/ui/toaster";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

function App() {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPortfolioData = async () => {
      try {
        setLoading(true);
        
        // Fetch all portfolio data in parallel
        const [profileRes, experienceRes, testimonialsRes, expertiseRes] = await Promise.all([
          fetch(`${BACKEND_URL}/api/profile`),
          fetch(`${BACKEND_URL}/api/experience`),
          fetch(`${BACKEND_URL}/api/testimonials`),
          fetch(`${BACKEND_URL}/api/expertise`)
        ]);

        const [profileData, experienceData, testimonialsData, expertiseData] = await Promise.all([
          profileRes.json(),
          experienceRes.json(),
          testimonialsRes.json(),
          expertiseRes.json()
        ]);

        // Combine all data
        const combinedData = {
          personal: profileData.data.personal,
          experience: experienceData.data,
          testimonials: testimonialsData.data,
          truffleExpertise: expertiseData.data
        };

        setPortfolioData(combinedData);
      } catch (err) {
        console.error('Error fetching portfolio data:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPortfolioData();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-amber-400 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-slate-300 text-lg">Loading portfolio...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <div className="text-center text-red-400">
          <p className="text-xl mb-4">Error loading portfolio</p>
          <p>{error}</p>
          <button 
            onClick={() => window.location.reload()} 
            className="mt-4 px-4 py-2 bg-amber-500 text-slate-900 rounded hover:bg-amber-600"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  if (!portfolioData) {
    return null;
  }

  return (
    <div className="App">
      <Header />
      <HeroSection data={portfolioData.personal} />
      <ExperienceSection experiences={portfolioData.experience} />
      <TruffleExpertiseSection expertise={portfolioData.truffleExpertise} />
      <TestimonialsSection testimonials={portfolioData.testimonials} />
      <ContactSection />
      <Footer />
      <Toaster />
    </div>
  );
}

export default App;