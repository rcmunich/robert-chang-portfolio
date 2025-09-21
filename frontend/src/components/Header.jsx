import React from 'react';
import { Button } from './ui/button';

const Header = () => {
  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-slate-900/95 backdrop-blur-sm border-b border-slate-800">
      <div className="container mx-auto px-6 py-4">
        <nav className="flex items-center justify-between">
          <div className="text-xl font-bold text-amber-400">
            Robert Chang
          </div>
          
          <div className="hidden md:flex items-center space-x-8">
            <button
              onClick={() => scrollToSection('about')}
              className="text-slate-300 hover:text-amber-400 transition-colors duration-200"
            >
              About
            </button>
            <button
              onClick={() => scrollToSection('experience')}
              className="text-slate-300 hover:text-amber-400 transition-colors duration-200"
            >
              Experience
            </button>
            <button
              onClick={() => scrollToSection('expertise')}
              className="text-slate-300 hover:text-amber-400 transition-colors duration-200"
            >
              Expertise
            </button>
            <button
              onClick={() => scrollToSection('testimonials')}
              className="text-slate-300 hover:text-amber-400 transition-colors duration-200"
            >
              Testimonials
            </button>
            <Button
              onClick={() => scrollToSection('contact')}
              className="bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold px-6 py-2 rounded-full transition-all duration-200 transform hover:scale-105"
            >
              Contact
            </Button>
          </div>
        </nav>
      </div>
    </header>
  );
};

export default Header;