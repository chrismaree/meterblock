<template>
  <div class="ViewAllMeters">
    <h1>All Meters Graphs</h1>

         <div class="sub-title">Select Meters to add</div>
        
        <el-select filterable v-model="inputMeter" placeholder="Select address to mint">
            <div v-for="meter in allMeterAddresses">
                <el-option :label="meter" :value="meter"></el-option>
            </div>      
        </el-select>
        <el-button @click="handleSelect" type="primary">Add</el-button>
        <br>
        <el-tag
            v-for="tag in tags"
            :key="tag.name"
            closable
            :type="tag.type"
              @close="handleClose(tag)">
            {{tag.name}}
        </el-tag>
        <br>
        {{meterData}}
        
        <br>
        <el-radio-group v-model="chartMode">
        <el-radio-button label="Minute"></el-radio-button>
        <el-radio-button label="Hour"></el-radio-button>
        <el-radio-button label="Day"></el-radio-button>
        <el-radio-button label="Week"></el-radio-button>
        <el-radio-button label="Month"></el-radio-button>
    </el-radio-group>
  </div>
</template>

<script>
import Bar from "./BarChart.js";
import store from "../store";

import { loadKragToken, getAllMeters } from "../../utils/KraGTokenInterface";

export default {
  name: "ViewAllMeters",
  data() {
    return {
      allMeterAddresses: [],
      tags: [],
      inputMeter: "",
      chartMode: "Hour",
      selectedMeters: [],
      tagTypes: ["", "success", "info", "warning", "danger"],
      meterData: {}
    };
  },
  async created() {
    await loadKragToken();
    this.allMeterAddresses = await getAllMeters();
  },
  methods: {
    async addMeter(_meterAddress) {
      console.log(_meterAddress);
      let lables = [];
      let values = [];
      let tokens = [];
      await this.$gun
        .get(_meterAddress)
        .map()
        .on(function(value, time) {
          lables.push(time);
          values.push(value.power);
          tokens.push(value.tokens);
        });
      if (this.$data.meterData[_meterAddress] == undefined) {
        this.$data.meterData[_meterAddress] = {
          lables: [],
          values: [],
          tokens: []
        };
      }
      this.$data.meterData[_meterAddress].lables.push(lables);
      this.$data.meterData[_meterAddress].values.push(values);
      this.$data.meterData[_meterAddress].tokens.push(tokens);
    },
    handleClose(tag) {
      this.tags.splice(this.tags.indexOf(tag), 1);
      this.selectedMeters.splice(this.tags.indexOf(tag), 1);
      this.inputMeter = "";
    },
    handleSelect() {
      if (
        this.selectedMeters.includes(this.inputMeter) ||
        this.inputMeter == ""
      ) {
        console.log("Address already added");
      } else {
        this.selectedMeters.push(this.inputMeter);
        this.tags.push({
          name: this.inputMeter,
          type: this.tagTypes[this.selectedMeters.length - 1]
        });
        this.addMeter(this.inputMeter);
      }
    }
  },

  computed: {
    datacollection() {
      try {
        let number;
        let timeStamps = [];
        if (this.chartMode == "Minute") {
          if (this.$data.meterData.lables[0].length > 30) {
            number = 30;
          } else number = number = this.$data.meterData.lables[0].length;

          for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
            Math.max(this.$data.meterData.lables[0].length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "hour"));
          }
        }

        if (this.chartMode == "Hour") {
          if (this.$data.meterData.lables[0].length > 1800) {
            number = 1800;
          } else number = number = this.$data.meterData.lables[0].length;
          for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
            Math.max(this.$data.meterData.lables[0].length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "hour"));
          }
        }

        if (this.chartMode == "Day") {
          if (this.$data.meterData.lables[0].length > 43200) {
            number = 43200;
          } else number = number = this.$data.meterData.lables[0].length;
          for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
            Math.max(this.$data.meterData.lables[0].length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "day"));
          }
        }

        if (this.chartMode == "Week") {
          if (this.$data.meterData.lables[0].length > 302400) {
            number = 302400;
          } else number = number = this.$data.meterData.lables[0].length;
          for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
            Math.max(this.$data.meterData.lables[0].length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "month"));
          }
        }

        if (this.chartMode == "Month") {
          if (this.$data.meterData.lables[0].length > 1296000) {
            number = 1296000;
          } else number = number = this.$data.meterData.lables[0].length;
          for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
            Math.max(this.$data.meterData.lables[0].length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "month"));
          }
        }

        return {
          labels: timeStamps,
          datasets: [
            {
              label: this.selectedMeter + " Power Consumption",
              data: this.$data.meterData.values[0].slice(
                Math.max(this.$data.meterData.lables[0].length - number, 0)
              ),
              backgroundColor: Array.apply(null, Array(number)).map(
                String.prototype.valueOf,
                "#7ea9d6"
              )
            }
          ]
        };
      } catch (e) {
        console.log(e);
        return null;
      }
    }
  }
};
</script>

<style scoped lang="scss">
.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
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
