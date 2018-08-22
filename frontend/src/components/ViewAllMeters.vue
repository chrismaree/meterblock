<template>
  <div class="ViewAllMeters">
    <h1>All Meters Graphs</h1>

         <div class="sub-title">Select Meters to add</div>
        <el-autocomplete
        class="inline-input"
        v-model="inputMeter"
        :fetch-suggestions="querySearch"
        placeholder="Please Input"
        @select="handleSelect"
        ></el-autocomplete>
        
        <el-select filterable v-model="formInline.viewAddress" placeholder="Select address to mint">
            <div v-for="meter in allMeterAddresses">
                <el-option :label="meter" :value="meter"></el-option>
            </div>      
        </el-select>
        <el-button @click="handleSelect" type="primary">Add</el-button>
        <br><br>
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
      inputMeter: "",
      chartMode: "Hour"
    };
  },
  async created() {
    this.allMeterAddresses = await loadKragToken();
    let allAddresses = await getAllMeters();
    for (let i = 0; i < allAddresses.length; i++) {
      this.allMeterAddresses.push({ value: allAddresses[i] });
    }
  },
  methods: {
    addMeter() {},
    handleSelect() {
      console.log("item");
    },
    querySearch(queryString, cb) {
      var links = this.allMeterAddresses;
      var results = queryString
        ? links.filter(this.createFilter(queryString))
        : links;
      // call callback function to return suggestion objects
      cb(results);
    },
    createFilter(queryString) {
      return link => {
        return (
          link.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        );
      };
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
