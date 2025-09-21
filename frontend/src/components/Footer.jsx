import React from 'react';
import { Separator } from './ui/separator';
import { Badge } from './ui/badge';
import { Linkedin, Mail, Globe, Award } from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  const socialLinks = [
    {
      icon: <Linkedin className="w-5 h-5" />,
      href: 'https://linkedin.com/in/robertchang',
      label: 'LinkedIn'
    },
    {
      icon: <Mail className="w-5 h-5" />,
      href: 'mailto:robert@example.com',
      label: 'Email'
    },
    {
      icon: <Globe className="w-5 h-5" />,
      href: '#',
      label: 'Website'
    }
  ];

  const achievements = [
    'Stanford MBA',
    'Robert Bosch Foundation Fellow',
    '17+ Years Truffle Innovation',
    'Global Business Leader'
  ];

  return (
    <footer className="bg-slate-900 border-t border-slate-800">
      <div className="container mx-auto px-6 py-12">
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* Profile Summary */}
          <div className="lg:col-span-2">
            <h3 className="text-2xl font-bold text-white mb-4">
              <span className="text-amber-400">Robert</span> Chang
            </h3>
            <p className="text-slate-300 mb-4 leading-relaxed">
              Managing Director & Chief Truffle Officer combining technology leadership 
              with innovative agriculture. Stanford MBA with global business experience 
              across three continents.
            </p>
            <div className="flex flex-wrap gap-2 mb-6">
              {achievements.map((achievement, index) => (
                <Badge key={index} variant="outline" className="border-amber-400 text-amber-400 bg-amber-400/10">
                  <Award className="w-3 h-3 mr-1" />
                  {achievement}
                </Badge>
              ))}
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-lg font-semibold text-white mb-4">Quick Links</h4>
            <ul className="space-y-2">
              {[
                { name: 'About', href: '#hero' },
                { name: 'Experience', href: '#experience' },
                { name: 'Expertise', href: '#expertise' },
                { name: 'Testimonials', href: '#testimonials' },
                { name: 'Contact', href: '#contact' }
              ].map((link) => (
                <li key={link.name}>
                  <a
                    href={link.href}
                    className="text-slate-400 hover:text-amber-400 transition-colors duration-200"
                    onClick={(e) => {
                      e.preventDefault();
                      document.getElementById(link.href.slice(1))?.scrollIntoView({ behavior: 'smooth' });
                    }}
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact & Social */}
          <div>
            <h4 className="text-lg font-semibold text-white mb-4">Connect</h4>
            <div className="space-y-3 mb-6">
              <div className="text-slate-400">
                <div className="text-sm">Location</div>
                <div className="text-white">San Francisco, CA</div>
              </div>
              <div className="text-slate-400">
                <div className="text-sm">Languages</div>
                <div className="text-white text-sm">English, German, Mandarin, Japanese, Spanish</div>
              </div>
            </div>
            
            <div className="flex gap-3">
              {socialLinks.map((link, index) => (
                <a
                  key={index}
                  href={link.href}
                  className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center text-slate-400 hover:text-amber-400 hover:bg-slate-700 transition-all duration-200 transform hover:scale-110"
                  aria-label={link.label}
                >
                  {link.icon}
                </a>
              ))}
            </div>
          </div>
        </div>

        <Separator className="my-8 bg-slate-800" />

        <div className="flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="text-slate-400 text-sm">
            © {currentYear} Robert Chang. All rights reserved.
          </div>
          <div className="text-slate-400 text-sm">
            Built with passion for innovation and excellence.
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;