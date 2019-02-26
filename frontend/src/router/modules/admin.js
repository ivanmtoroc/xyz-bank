import Base from '@/components/admin/Base'

import UsersTable from '@/components/admin/apps/users/Table'

export default {
  path: '/admin',
  name: 'admin',
  component: Base,
  children: [
    { path: 'users', name: 'users', component: UsersTable }
  ]
}