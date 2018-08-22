<template>
  <div class="hello">
    <h1> Meter Account Management </h1>
<el-row>
  <el-col :span="12">
<p>Your web3 account has {{accountBalance/100000}} KraG Tokens.</p>
    <div v-if="selectedMeter!=''">
    <p>Transfer tokens to Meter from account <el-input v-model="loadValue" type="number" min=0 :step="1"></el-input>Tokens(1 KraG = 1 kWh)</p>
    <el-button type="primary" @click="loadTokensToMeter" :disabled="accountBalance==0">Load</el-button>
</div>
<div v-if="selectedMeter==''">
        Please select a meter to load tokens to it
    </div>

  </el-col>
  <el-col :span="12">
      <div v-if="selectedMeter!=''">
      <p>The selected Meter has {{meterBalance/100000}} KraG Tokens. Transfer tokens from meter to account</p>
      {{selectedMeter}}
    <el-button type="primary" :disabled="meterBalance==0">Withdraw</el-button>
    </div>
    <div v-if="selectedMeter==''">
        Please select a meter to view it's balance
    </div>
  </el-col>
</el-row>

    
    
  </div>
</template>

<script>
import {
  loadKragToken,
  balanceOfCurrentAddress,
  balanceOf,
  transfer
} from "../../utils/KraGTokenInterface";

export default {
  name: "MeterAccountManagement",
  props: {
    selectedMeter: String
  },
  data() {
    return {
      accountBalance: 0,
      loadValue: 0,
      withDrawValue: 0,
      meterBalance: 0
    };
  },
  methods: {
    async loadTokensToMeter() {
      console.log(this.selectedMeter);
      await transfer(this.selectedMeter, this.loadValue);
    },

    async withdrawTokensFromMeter() {

    },
  },
  async mounted() {
    await loadKragToken();
    this.accountBalance = parseInt(await balanceOfCurrentAddress());
    this.meterBalance = parseInt(await balanceOf(this.selectedMeter));
  }
};
</script>

<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
