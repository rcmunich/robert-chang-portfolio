import React from "react";
import "./App.css";
import { portfolioData } from "./data/mock";
import Header from "./components/Header";
import HeroSection from "./components/HeroSection";
import ExperienceSection from "./components/ExperienceSection";
import TruffleExpertiseSection from "./components/TruffleExpertiseSection";
import TestimonialsSection from "./components/TestimonialsSection";
import ContactSection from "./components/ContactSection";
import Footer from "./components/Footer";
import { Toaster } from "./components/ui/toaster";

function App() {
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