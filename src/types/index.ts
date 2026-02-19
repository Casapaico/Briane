export interface NavItem {
  label: string;
  href: string;
  external?: boolean;
  children?: NavItem[];
}

export interface Service {
  id: string;
  name: string;
  slug: string;
  shortDescription: string;
  description: string;
  features: string[];
  image?: string;
  icon?: string;
}

export interface TeamMember {
  name: string;
  position: string;
  image?: string;
  bio?: string;
}

export interface Stat {
  value: string;
  label: string;
  suffix?: string;
}

export interface Client {
  name: string;
  logo: string;
}

export interface NewsItem {
  title: string;
  slug: string;
  excerpt: string;
  date: string;
  image?: string;
  category?: string;
}

export interface ContactInfo {
  address: string;
  phone: string[];
  email: string[];
  hours: string;
}

export interface SocialLink {
  platform: string;
  url: string;
  icon: string;
}

export interface CompanyInfo {
  name: string;
  tagline: string;
  description: string;
  mission: string;
  vision: string;
  values: { title: string; description: string }[];
  contact: ContactInfo;
  social: SocialLink[];
}

export interface SEOProps {
  title: string;
  description: string;
  image?: string;
  canonical?: string;
  noindex?: boolean;
}
