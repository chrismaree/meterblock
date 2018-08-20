<template>
  <div class="Administrator">
<el-row :gutter="20">
  <el-col :span="12" :offset="6">
     <el-table
      :data="tableData"
      style="width: 100%">
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
  getDecimals
} from "../../utils/KraGTokenInterface";

export default {
  name: "Administrator",
  data() {
    return {
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
      this.tableData[2].property = await getName(),
      this.tableData[3].property = await getSymbol(),
      this.tableData[4].property = await getTotalSupply(),
      this.tableData[5].property = await getDecimals();
    }
  },
  async created() {
    await loadKragToken();
    await this.loadTokenInfo()
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
