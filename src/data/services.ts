import type { Service } from '../types';

export const services: Service[] = [
  {
    id: 'supervan',
    name: 'SUPERVAN',
    slug: 'supervan',
    shortDescription: 'Transporte de carga pesada - Transportando la mayor carga',
    description:
      'Brindamos servicios de transporte de carga pesada atendiendo a principales sectores del país. Desde 1982 con servicio especializado en transporte portuario y operaciones mineras.',
    features: [
      'Servicios Portuarios desde 1982',
      'Operación Minera con flota ecológica GNV',
      'Monitoreo GPS 24/7 los 365 días',
      'Permisos IQBF y Matpel',
      'Coordinadores en puntos de carga y descarga',
      'Seguro de Transporte con Responsabilidad Civil',
      'Control Satelital de unidades',
      'Altos estándares en calidad, seguridad y medio ambiente',
    ],
    image: '/images/servicios/supervan.jpg',
    icon: 'truck',
  },
  {
    id: 'almacenes',
    name: 'ALMACENES DIEF',
    slug: 'almacenes',
    shortDescription: 'Almacenamiento seguro y eficiente',
    description:
      'Infraestructura de almacenamiento de primer nivel con sistemas de gestión avanzados para optimizar la cadena de suministro de su empresa.',
    features: [
      'Almacenes climatizados',
      'Sistema WMS integrado',
      'Control de inventario en tiempo real',
      'Seguridad 24/7 con CCTV',
      'Picking y packing',
      'Cross-docking',
      'Gestión de devoluciones',
      'Ubicación estratégica',
    ],
    image: '/images/servicios/almacenes.jpg',
    icon: 'warehouse',
  },
];

export const getServiceBySlug = (slug: string): Service | undefined => {
  return services.find((service) => service.slug === slug);
};
