<template>
  <div class="meterusage">
  <h1>Meter Management</h1>
  <p>You have {{numberOfMetersToOwner}} meters registered to your address</p>
    <div v-if="numberOfMetersToOwner>0">{{metersToOwner}}</div>
    <p>Select Meter to manage</p>
    <el-select filterable v-model="selectedMeter" placeholder="Select address to mint">
      <div v-for="meter in metersToOwner">
        <el-option :label="meter" :value="meter"></el-option>
      </div>      
    </el-select>

    <MeterAccountManagement :selectedMeter="selectedMeter"/>
    <UsageChart :selectedMeter="selectedMeter"/>
  </div>
</template>

<script>
import {
  loadKragToken,
  getMetersToOwner
} from "../../utils/KraGTokenInterface";

import UsageChart from '@/components/UsageChart.vue'
import MeterAccountManagement from '@/components/MeterAccountManagement.vue'

export default {
  name: 'MeterManagement',
  data() {
    return {
      metersToOwner: [],
      selectedMeter: "",
      numberOfMetersToOwner: 0
    }
  },
  components: {
    UsageChart,
    MeterAccountManagement
  },
  async mounted () {
      await loadKragToken()
      this.metersToOwner = await getMetersToOwner()
      this.numberOfMetersToOwner = this.metersToOwner.length
  }
}
</script>
