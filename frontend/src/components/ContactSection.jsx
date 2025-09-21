import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Textarea } from './ui/textarea';
import { Badge } from './ui/badge';
import { Mail, Phone, MapPin, Linkedin, Send, CheckCircle } from 'lucide-react';
import { useToast } from '../hooks/use-toast';

const ContactSection = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
    inquiryType: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const { toast } = useToast();

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    // Simulate form submission
    setTimeout(() => {
      toast({
        title: "Message Sent!",
        description: "Thank you for your interest. I'll get back to you within 24 hours.",
      });
      setFormData({
        name: '',
        email: '',
        subject: '',
        message: '',
        inquiryType: ''
      });
      setIsSubmitting(false);
    }, 2000);
  };

  const inquiryTypes = [
    'Business Partnership',
    'Executive Opportunity',
    'Truffle Collaboration',
    'Consulting Services',
    'Other'
  ];

  const contactInfo = [
    {
      icon: <Mail className="w-5 h-5" />,
      label: 'Email',
      value: 'robert@example.com',
      href: 'mailto:robert@example.com'
    },
    {
      icon: <Phone className="w-5 h-5" />,
      label: 'Phone',
      value: '+1 (415) 555-0123',
      href: 'tel:+14155550123'
    },
    {
      icon: <MapPin className="w-5 h-5" />,
      label: 'Location',
      value: 'San Francisco, CA',
      href: null
    },
    {
      icon: <Linkedin className="w-5 h-5" />,
      label: 'LinkedIn',
      value: 'linkedin.com/in/robertchang',
      href: 'https://linkedin.com/in/robertchang'
    }
  ];

  return (
    <section id="contact" className="py-20 bg-slate-900">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Let's <span className="text-amber-400">Connect</span>
          </h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto">
            Ready to explore opportunities? I'm always interested in discussing business partnerships, 
            executive roles, and innovative projects.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 max-w-6xl mx-auto">
          {/* Contact Form */}
          <Card className="bg-slate-800 border-slate-700">
            <CardHeader>
              <CardTitle className="text-2xl text-white flex items-center gap-2">
                <Send className="w-6 h-6 text-amber-400" />
                Send a Message
              </CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-slate-300 text-sm font-medium mb-2">
                      Your Name
                    </label>
                    <Input
                      name="name"
                      value={formData.name}
                      onChange={handleInputChange}
                      placeholder="John Doe"
                      required
                      className="bg-slate-700 border-slate-600 text-white placeholder-slate-400"
                    />
                  </div>
                  <div>
                    <label className="block text-slate-300 text-sm font-medium mb-2">
                      Email Address
                    </label>
                    <Input
                      type="email"
                      name="email"
                      value={formData.email}
                      onChange={handleInputChange}
                      placeholder="john@example.com"
                      required
                      className="bg-slate-700 border-slate-600 text-white placeholder-slate-400"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-slate-300 text-sm font-medium mb-2">
                    Inquiry Type
                  </label>
                  <div className="flex flex-wrap gap-2">
                    {inquiryTypes.map((type) => (
                      <Badge
                        key={type}
                        variant={formData.inquiryType === type ? "default" : "outline"}
                        className={`cursor-pointer transition-colors duration-200 ${
                          formData.inquiryType === type
                            ? 'bg-amber-500 text-slate-900'
                            : 'border-slate-600 text-slate-300 hover:bg-slate-700'
                        }`}
                        onClick={() => setFormData(prev => ({ ...prev, inquiryType: type }))}
                      >
                        {type}
                      </Badge>
                    ))}
                  </div>
                </div>

                <div>
                  <label className="block text-slate-300 text-sm font-medium mb-2">
                    Subject
                  </label>
                  <Input
                    name="subject"
                    value={formData.subject}
                    onChange={handleInputChange}
                    placeholder="Brief subject line"
                    required
                    className="bg-slate-700 border-slate-600 text-white placeholder-slate-400"
                  />
                </div>

                <div>
                  <label className="block text-slate-300 text-sm font-medium mb-2">
                    Message
                  </label>
                  <Textarea
                    name="message"
                    value={formData.message}
                    onChange={handleInputChange}
                    placeholder="Tell me about your project, opportunity, or how we might collaborate..."
                    rows={5}
                    required
                    className="bg-slate-700 border-slate-600 text-white placeholder-slate-400"
                  />
                </div>

                <Button
                  type="submit"
                  disabled={isSubmitting}
                  className="w-full bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold py-3 rounded-lg transition-all duration-200 transform hover:scale-105"
                >
                  {isSubmitting ? (
                    <div className="flex items-center gap-2">
                      <div className="w-4 h-4 border-2 border-slate-900 border-t-transparent rounded-full animate-spin"></div>
                      Sending...
                    </div>
                  ) : (
                    <div className="flex items-center gap-2">
                      <Send className="w-4 h-4" />
                      Send Message
                    </div>
                  )}
                </Button>
              </form>
            </CardContent>
          </Card>

          {/* Contact Information */}
          <div className="space-y-8">
            <Card className="bg-slate-800 border-slate-700">
              <CardHeader>
                <CardTitle className="text-2xl text-white">
                  Contact Information
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                {contactInfo.map((info, index) => (
                  <div key={index} className="flex items-center gap-4 p-4 rounded-lg bg-slate-900/50 hover:bg-slate-900 transition-colors duration-200">
                    <div className="text-amber-400 flex-shrink-0">
                      {info.icon}
                    </div>
                    <div>
                      <div className="text-slate-400 text-sm">{info.label}</div>
                      {info.href ? (
                        <a
                          href={info.href}
                          className="text-white hover:text-amber-400 transition-colors duration-200"
                        >
                          {info.value}
                        </a>
                      ) : (
                        <div className="text-white">{info.value}</div>
                      )}
                    </div>
                  </div>
                ))}
              </CardContent>
            </Card>

            <Card className="bg-gradient-to-br from-amber-500/10 to-amber-600/10 border-amber-500/20">
              <CardContent className="pt-6">
                <div className="flex items-start gap-3 mb-4">
                  <CheckCircle className="w-6 h-6 text-amber-400 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-white font-semibold mb-2">Response Time</h3>
                    <p className="text-slate-300 text-sm">
                      I typically respond to inquiries within 24 hours. For urgent matters, 
                      please mention it in your subject line.
                    </p>
                  </div>
                </div>
                <div className="flex items-start gap-3">
                  <CheckCircle className="w-6 h-6 text-amber-400 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-white font-semibold mb-2">Availability</h3>
                    <p className="text-slate-300 text-sm">
                      Open to discussing board positions, executive roles, strategic partnerships, 
                      and innovative agricultural projects.
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;