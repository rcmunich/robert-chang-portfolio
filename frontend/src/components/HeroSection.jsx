import React from 'react';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { MapPin, Languages, Award } from 'lucide-react';

const HeroSection = ({ data }) => {
  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section id="hero" className="relative min-h-screen flex items-center bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Background Pattern */}
      <div className="absolute inset-0 opacity-20">
        <div className="w-full h-full" style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23334155' fill-opacity='0.05'%3E%3Cpath d='m36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`
        }}></div>
      </div>
      
      <div className="container mx-auto px-6 py-20 relative z-10">
        <div className="max-w-4xl">
          <div className="flex items-center gap-2 mb-4">
            <Badge variant="outline" className="border-amber-400 text-amber-400 bg-amber-400/10">
              <Award className="w-3 h-3 mr-1" />
              Stanford MBA
            </Badge>
            <Badge variant="outline" className="border-amber-400 text-amber-400 bg-amber-400/10">
              <MapPin className="w-3 h-3 mr-1" />
              {data.location}
            </Badge>
          </div>
          
          <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
            <span className="text-amber-400">Robert</span> Chang
          </h1>
          
          <div className="text-xl md:text-2xl text-slate-300 mb-4 font-medium">
            {data.title}
          </div>
          
          <div className="text-lg text-amber-400 mb-8 font-semibold">
            {data.company}
          </div>
          
          <p className="text-lg text-slate-300 leading-relaxed mb-8 max-w-3xl">
            {data.summary}
          </p>
          
          <div className="flex items-center gap-2 mb-10">
            <Languages className="w-5 h-5 text-amber-400" />
            <span className="text-slate-400 text-sm">Fluent in:</span>
            <div className="flex gap-2">
              {data.languages.map((lang, index) => (
                <Badge key={index} variant="secondary" className="bg-slate-800 text-slate-300">
                  {lang}
                </Badge>
              ))}
            </div>
          </div>
          
          <div className="flex flex-col sm:flex-row gap-4">
            <Button
              onClick={() => scrollToSection('experience')}
              size="lg"
              className="bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold px-8 py-3 rounded-full transition-all duration-200 transform hover:scale-105 shadow-lg hover:shadow-amber-500/25"
            >
              View Experience
            </Button>
            <Button
              onClick={() => scrollToSection('contact')}
              variant="outline"
              size="lg"
              className="border-2 border-amber-400 text-amber-400 hover:bg-amber-400 hover:text-slate-900 font-semibold px-8 py-3 rounded-full transition-all duration-200 transform hover:scale-105"
            >
              Get In Touch
            </Button>
          </div>
        </div>
      </div>
      
      {/* Scroll Indicator */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
        <div className="w-6 h-10 border-2 border-amber-400 rounded-full flex justify-center">
          <div className="w-1 h-3 bg-amber-400 rounded-full mt-2 animate-pulse"></div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;