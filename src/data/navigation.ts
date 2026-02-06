import type { NavItem } from '../types';

export const mainNavigation: NavItem[] = [
  {
    label: 'Inicio',
    href: '/',
  },
  {
    label: 'BRIANE',
    href: '/briane',
  },
  {
    label: 'Servicios',
    href: '/servicios',
    children: [
      {
        label: 'SUPERVAN',
        href: '/servicios/supervan',
      },
      {
        label: 'ALMACENES DIEF',
        href: '/servicios/almacenes',
      },
    ],
  },
  {
    label: 'Valor Agregado',
    href: '/valor-agregado',
  },
  {
    label: 'Más',
    href: '#',
    children: [
      {
        label: 'Estándares de Gestión',
        href: '/estandares-gestion',
      },
      {
        label: 'Políticas',
        href: '/politicas',
      },
      {
        label: 'Trabaja con Nosotros',
        href: '/trabaja-con-nosotros',
      },
      {
        label: 'Noticias',
        href: '/noticias',
      },
    ],
  },
];

export const footerNavigation = {
  servicios: [
    { label: 'SUPERVAN', href: '/servicios/supervan' },
    { label: 'ALMACENES DIEF', href: '/servicios/almacenes' },
  ],
  empresa: [
    { label: 'Sobre BRIANE', href: '/briane' },
    { label: 'Valor Agregado', href: '/valor-agregado' },
    { label: 'Estándares de Gestión', href: '/estandares-gestion' },
    { label: 'Politicas', href: '/politicas' },
  ],
  recursos: [
    { label: 'Noticias', href: '/noticias' },
    { label: 'Trabaja con Nosotros', href: '/trabaja-con-nosotros' },
    { label: 'Contactenos', href: '/contactenos' },
  ],
};
