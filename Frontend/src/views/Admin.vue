<template>
  <div class="Administrator">
    <AdministratorTable/>
  </div>
</template>

<script>
import AdministratorTable from '@/components/AdministratorTable.vue'

export default {
  name: 'Admin',
  components: {
    AdministratorTable,
  }
}
</script>
