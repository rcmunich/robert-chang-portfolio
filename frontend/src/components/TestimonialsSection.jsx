import React from 'react';
import { Card, CardContent } from './ui/card';
import { Avatar, AvatarImage, AvatarFallback } from './ui/avatar';
import { Quote } from 'lucide-react';

const TestimonialsSection = ({ testimonials }) => {
  return (
    <section id="testimonials" className="py-20 bg-slate-50">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
            What Leaders <span className="text-amber-600">Say</span>
          </h2>
          <p className="text-xl text-slate-600 max-w-3xl mx-auto">
            Testimonials from industry leaders, partners, and collaborators
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {testimonials.map((testimonial) => (
            <Card key={testimonial.id} className="bg-white border-0 shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2 relative overflow-hidden">
              {/* Quote icon background */}
              <div className="absolute top-4 right-4 text-amber-100">
                <Quote className="w-12 h-12" fill="currentColor" />
              </div>
              
              <CardContent className="pt-8 pb-6">
                <div className="flex items-center gap-4 mb-6">
                  <Avatar className="w-14 h-14 ring-2 ring-amber-200">
                    <AvatarImage src={testimonial.avatar} alt={testimonial.name} />
                    <AvatarFallback className="bg-amber-100 text-amber-800 font-semibold">
                      {testimonial.name.split(' ').map(n => n[0]).join('')}
                    </AvatarFallback>
                  </Avatar>
                  <div>
                    <h4 className="font-semibold text-slate-900">{testimonial.name}</h4>
                    <p className="text-sm text-slate-600">{testimonial.title}</p>
                  </div>
                </div>
                
                <blockquote className="text-slate-700 leading-relaxed italic relative z-10">
                  "{testimonial.content}"
                </blockquote>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TestimonialsSection;