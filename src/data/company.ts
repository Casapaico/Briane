import type { CompanyInfo, Stat, Client, TeamMember } from '../types';

export const companyInfo: CompanyInfo = {
  name: 'BRIANE',
  tagline: 'Transporte Logístico y Almacenamiento',
  description:
    'Somos una empresa peruana líder en servicios de transporte logístico y almacenamiento, comprometida con la excelencia operativa y la satisfacción de nuestros clientes.',
  mission:
    'Brindar soluciones logísticas integrales de alta calidad, optimizando la cadena de suministro de nuestros clientes mediante servicios de transporte y almacenamiento confiables, seguros y eficientes.',
  vision:
    'Ser reconocidos como la empresa líder en soluciones logísticas del Perú, destacando por nuestra innovación tecnológica, excelencia operativa y compromiso con el desarrollo sostenible.',
  values: [
    {
      title: 'Compromiso',
      description:
        'Nos comprometemos con cada cliente, garantizando el cumplimiento de nuestras promesas.',
    },
    {
      title: 'Integridad',
      description:
        'Actuamos con transparencia y honestidad en todas nuestras operaciones.',
    },
    {
      title: 'Excelencia',
      description:
        'Buscamos la mejora continua en cada proceso para superar las expectativas.',
    },
    {
      title: 'Innovación',
      description:
        'Implementamos tecnología de vanguardia para optimizar nuestros servicios.',
    },
    {
      title: 'Responsabilidad',
      description:
        'Operamos con responsabilidad social y ambiental en todas nuestras actividades.',
    },
    {
      title: 'Trabajo en Equipo',
      description:
        'Fomentamos la colaboración y el respeto mutuo entre todos los miembros de nuestra organización.',
    },
  ],
  contact: {
    address: 'Av. Elmer Faucett N° 5104, Urb. Las Fresas, Callao, Perú',
    phone: ['+51 998 109 252', '+51 994 076 151'],
    email: ['alvaro.villabos@supervan.pe', 'comercial@supervan.pe'],
    hours: 'Lunes a Viernes: 8:00 AM - 6:00 PM',
  },
  social: [
    {
      platform: 'Facebook',
      url: 'https://www.facebook.com/transportesbriane?ref=embed_page',
      icon: 'facebook',
    },
    {
      platform: 'LinkedIn',
      url: 'https://linkedin.com/company/brianeperu',
      icon: 'linkedin',
    },
  ],
};

export const stats: Stat[] = [
  {
    value: '40',
    label: 'Años de Experiencia',
    suffix: '+',
  },
  {
    value: '500',
    label: 'Clientes Satisfechos',
    suffix: '+',
  },
  {
    value: '100',
    label: 'Unidades de Flota',
    suffix: '+',
  },
  {
    value: '50000',
    label: 'm2 de Almacenes',
    suffix: '+',
  },
];

export const clients: Client[] = [
  { name: 'Cliente 1', logo: '/images/clientes/channels4_profile.jpg' },
  { name: 'Cliente 2', logo: '/images/clientes/cusa1-removebg-preview.png' },
  { name: 'Cliente 3', logo: '/images/clientes/images-removebg-preview.png' },
  { name: 'Cliente 4', logo: '/images/clientes/logo.png' },
  { name: 'Alicorp', logo: '/images/clientes/logo-alicorp.webp' },
  { name: 'Cliente 6', logo: '/images/clientes/logotipo_blue.svg' },
];

export const teamMembers: TeamMember[] = [
  {
    name: 'Juan Pérez',
    position: 'Gerente General',
    image: '/images/equipo/gerente-general.jpg',
    bio: 'Más de 20 años de experiencia en el sector logístico.',
  },
  {
    name: 'Maria Garcia',
    position: 'Directora de Operaciones',
    image: '/images/equipo/directora-operaciones.jpg',
    bio: 'Especialista en optimización de cadenas de suministro.',
  },
  {
    name: 'Carlos Rodriguez',
    position: 'Gerente Comercial',
    image: '/images/equipo/gerente-comercial.jpg',
    bio: 'Experto en desarrollo de negocios y relaciones con clientes.',
  },
];
