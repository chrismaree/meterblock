<template>
  <div class="Administrator">
    <el-row :gutter="20">
      <el-col :span="15" :offset="5">
        
<h1 class="center">Admin Controls</h1>

<el-form :inline="true" :model="formInline" class="demo-form-inline" label-width="120px">  
  <el-row>
    <el-col :span="24">
  <el-form-item label="Register Meter">
    <el-input v-model="formInline.registrerMeterAddress" placeholder="Meter Address"></el-input>
  </el-form-item>
  <i class="el-icon-arrow-right" style="padding-top:12px"></i>
  <el-form-item label="To Owner">
    <el-input v-model="formInline.registrerOwnerAddress" placeholder="Owner Address"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button @click="registerMeter" type="primary">Register</el-button>
  </el-form-item>
  </el-col>
  </el-row>
  
  <el-row>
    <el-col :span="24">
  <el-form-item label="Mint new Tokens">
    <el-select filterable v-model="formInline.mintAddress" placeholder="Select address to mint">
      <div v-for="meter in allMeters">
        <el-option :label="meter" :value="meter"></el-option>
      </div>      
    </el-select>
  </el-form-item>
  <el-form-item label="Tokens(kWh)">
    <el-input v-model="formInline.tokens" type="number" min=0 :step="1"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button @click="mintTokens" type="primary">Mint</el-button>
  </el-form-item>
</el-col>
  </el-row>

  <el-row>
    <el-col :span="24">
  <el-form-item label="Token Balance">
    <el-select filterable v-model="formInline.viewAddress" placeholder="Select address to mint">
      <div v-for="meter in allMeters">
        <el-option :label="meter" :value="meter"></el-option>
      </div>      
    </el-select>
  </el-form-item>
  <el-form-item>
    <el-button @click="viewBalance" type="primary">View</el-button>
    <el-button @click="mintTokens">View Usage</el-button>
  </el-form-item>
  </el-col>
  </el-row>
  <div v-if="meterOwner">    
  <el-row>
    <el-col :span="24">
      <strong>Balance:</strong> {{meterBalance}} <strong>Owner:</strong> {{meterOwner}}
    </el-col>
  </el-row>
  </div>
</el-form>
<br>
<h1 class="center">KraG Token Properties</h1>        
        <el-table
          :data="tableData"
          style="width: 100%"
          border>
          <el-table-column
            prop="value"
            label="Value"
            >
          </el-table-column>
          <el-table-column
            prop="property"
            label="Property"
            >
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import {
  loadKragToken,
  getOwnerAddress,
  getName,
  getSymbol,
  getTotalSupply,
  getDecimals,
  getAllMeters,
  mintTokensTo,
  registerMeter,
  balanceOf,
  meterOwnerOf
} from "../../utils/KraGTokenInterface";

export default {
  name: "AdministratorTable",
  data() {
    return {
      meterBalance: 0,
      meterOwner: "",
      allMeters: [],
      formInline: {
        registrerMeterAddress: "",
        registrerOwnerAddress: "",
        mintAddress: "",
        viewAddress: "",
        tokens: 0
      },
      tableData: [
        { value: "owner", property: "" },
        { value: "tokenContractAddress", property: "" },
        { value: "tokenName", property: "" },
        { value: "tokenSymbol", property: "" },
        { value: "tokenTotalSupply", property: "" },
        { value: "tokenDecimals", property: "" }
      ]
    };
  },
  methods: {
    async loadContract() {
      await loadKragToken();
    },

    async loadTokenInfo() {
      this.tableData[0].property = await getOwnerAddress();
      this.tableData[1].property = this.$store.state.kraGTokenAddress;
      this.tableData[2].property = await getName();
      this.tableData[3].property = await getSymbol();
      this.tableData[4].property = await getTotalSupply();
      this.tableData[5].property = await getDecimals();
    },

    async loadAllMeters() {
      this.allMeters = await getAllMeters();
    },

    async mintTokens() {
      await mintTokensTo(
        this.formInline.tokens * 100000,
        this.formInline.mintAddress
      );
    },

    async registerMeter() {
      await registerMeter(
        this.formInline.registrerMeterAddress,
        this.formInline.registrerOwnerAddress
      );
      await this.loadAllMeters();
    },
    async viewBalance() {
      this.meterBalance = await balanceOf(this.formInline.viewAddress);
      this.meterOwner = await meterOwnerOf(this.formInline.viewAddress);
    }
  },
  async created() {
    await loadKragToken();
    await this.loadTokenInfo();
    await this.loadAllMeters();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
