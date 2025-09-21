import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Building, Calendar, MapPin, CheckCircle } from 'lucide-react';

const ExperienceSection = ({ experiences }) => {
  return (
    <section id="experience" className="py-20 bg-slate-50">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
            Professional <span className="text-amber-600">Experience</span>
          </h2>
          <p className="text-xl text-slate-600 max-w-3xl mx-auto">
            Over two decades of leadership across technology, entrepreneurship, and innovative agriculture
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          {experiences.map((experience, index) => (
            <div key={experience.id} className="relative">
              {/* Timeline line */}
              {index < experiences.length - 1 && (
                <div className="absolute left-6 top-20 w-0.5 h-32 bg-amber-300 hidden md:block"></div>
              )}
              
              <Card className="mb-8 bg-white border-l-4 border-l-amber-500 shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                <CardHeader>
                  <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4">
                    <div className="flex-1">
                      <CardTitle className="text-2xl text-slate-900 mb-2">
                        {experience.position}
                      </CardTitle>
                      <div className="flex items-center gap-2 text-amber-600 font-semibold mb-2">
                        <Building className="w-4 h-4" />
                        {experience.company}
                      </div>
                      <div className="flex flex-col sm:flex-row sm:items-center gap-2 text-slate-600">
                        <div className="flex items-center gap-1">
                          <Calendar className="w-4 h-4" />
                          {experience.duration}
                        </div>
                        {experience.location && (
                          <>
                            <span className="hidden sm:inline text-slate-400">•</span>
                            <div className="flex items-center gap-1">
                              <MapPin className="w-4 h-4" />
                              {experience.location}
                            </div>
                          </>
                        )}
                      </div>
                    </div>
                    <Badge variant="secondary" className="bg-amber-100 text-amber-800 self-start">
                      {index === 0 ? 'Current' : 'Former'}
                    </Badge>
                  </div>
                </CardHeader>
                
                <CardContent>
                  <p className="text-slate-700 mb-6 leading-relaxed">
                    {experience.description}
                  </p>
                  
                  {experience.achievements && experience.achievements.length > 0 && (
                    <div>
                      <h4 className="font-semibold text-slate-900 mb-3">Key Achievements:</h4>
                      <ul className="space-y-2">
                        {experience.achievements.map((achievement, achievementIndex) => (
                          <li key={achievementIndex} className="flex items-start gap-2">
                            <CheckCircle className="w-4 h-4 text-green-600 mt-0.5 flex-shrink-0" />
                            <span className="text-slate-700">{achievement}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ExperienceSection;