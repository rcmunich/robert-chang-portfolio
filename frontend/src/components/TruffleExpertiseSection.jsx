import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Microscope, Leaf, Globe, TrendingUp, CheckCircle2, Award } from 'lucide-react';

const TruffleExpertiseSection = ({ expertise }) => {
  const iconMap = {
    0: <Award className="w-6 h-6" />,
    1: <Microscope className="w-6 h-6" />,
    2: <Leaf className="w-6 h-6" />,
    3: <Globe className="w-6 h-6" />
  };

  return (
    <section id="expertise" className="py-20 bg-slate-900">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <Badge className="bg-amber-500/20 text-amber-400 border-amber-400 mb-4">
            Innovation & Science
          </Badge>
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
            {expertise.title}
          </h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto mb-4">
            {expertise.subtitle}
          </p>
          <p className="text-slate-400 max-w-2xl mx-auto">
            {expertise.description}
          </p>
        </div>

        {/* Metrics Grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mb-16">
          {expertise.metrics.map((metric, index) => (
            <Card key={index} className="bg-slate-800 border-slate-700 text-center hover:bg-slate-750 transition-colors duration-200">
              <CardContent className="pt-6">
                <div className="text-amber-400 mb-2 flex justify-center">
                  {iconMap[index] || <TrendingUp className="w-6 h-6" />}
                </div>
                <div className="text-3xl font-bold text-white mb-1">
                  {metric.value}
                </div>
                <div className="text-slate-400 text-sm">
                  {metric.label}
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Achievements */}
        <Card className="bg-slate-800 border-slate-700 max-w-4xl mx-auto">
          <CardHeader>
            <CardTitle className="text-2xl text-white flex items-center gap-2">
              <Microscope className="w-6 h-6 text-amber-400" />
              Scientific & Business Achievements
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid md:grid-cols-2 gap-4">
              {expertise.achievements.map((achievement, index) => (
                <div key={index} className="flex items-start gap-3 p-4 rounded-lg bg-slate-900/50 hover:bg-slate-900 transition-colors duration-200">
                  <CheckCircle2 className="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" />
                  <span className="text-slate-300">{achievement}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Call to Action */}
        <div className="text-center mt-16">
          <div className="bg-gradient-to-r from-amber-500/10 to-amber-600/10 rounded-2xl p-8 border border-amber-500/20">
            <h3 className="text-2xl font-bold text-white mb-4">
              Interested in Truffle Innovation?
            </h3>
            <p className="text-slate-300 mb-6 max-w-2xl mx-auto">
              Discover how scientific innovation meets culinary excellence in sustainable truffle cultivation.
            </p>
            <button 
              onClick={() => document.getElementById('contact').scrollIntoView({ behavior: 'smooth' })}
              className="bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold px-8 py-3 rounded-full transition-all duration-200 transform hover:scale-105 shadow-lg hover:shadow-amber-500/25"
            >
              Explore Collaboration
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default TruffleExpertiseSection;