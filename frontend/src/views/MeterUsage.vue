<template>
  <div class="meterusage">
    <h1>Meter Usage</h1>
    <!-- <UsageChart msg="Welcome to Your Vue.js App"/> -->
    <UsageChart/>
  </div>
</template>

<script>
// @ is an alias to /src
import UsageChart from '@/components/UsageChart.vue'

export default {
  name: 'meterusage',
  components: {
    UsageChart
  }
}
</script>
