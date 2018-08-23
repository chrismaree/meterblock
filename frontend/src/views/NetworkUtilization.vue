<template>
  <div class="NetworkUtilization">
    <ViewAllMeters/>
  </div>
</template>

<script>
// @ is an alias to /src
import ViewAllMeters from '@/components/ViewAllMeters.vue'

export default {
  name: 'NetworkUtilization',
  components: {
    ViewAllMeters
  }
}
</script>
