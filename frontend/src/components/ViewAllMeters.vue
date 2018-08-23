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
        <br>
        {{datacollection}}
        
        <br>
        <el-radio-group v-model="chartMode">
        <el-radio-button label="Minute"></el-radio-button>
        <el-radio-button label="Hour"></el-radio-button>
        <el-radio-button label="Day"></el-radio-button>
        <el-radio-button label="Week"></el-radio-button>
        <el-radio-button label="Month"></el-radio-button>
    </el-radio-group>
<br>
<el-card class="box-card" shadow="always" >
    <Bar :options="chartOptions" :chart-data="datacollection" style="hight:800px !important"></Bar>
  </el-card>

  </div>
</template>

<script>
import Bar from "./BarChart.js";
import store from "../store";

import { loadKragToken, getAllMeters } from "../../utils/KraGTokenInterface";

export default {
  name: "ViewAllMeters",
  components: {
    Bar
  },
  data() {
    return {
      allMeterAddresses: [],
      tags: [],
      inputMeter: "",
      chartMode: "Hour",
      selectedMeters: [],
      tagTypes: ["", "success", "info", "warning", "danger"],
      backgroundColors: [
        "rgba(64, 158, 255,0.2)",
        "rgba(103, 194, 58,0.2)",
        "rgba(144, 147, 153,0.2)",
        "rgba(230, 162, 60,0.2)",
        "rgba(245, 108, 108,0.2)"
      ],
      borderColors: [
        "rgba(64, 158, 255,1)",
        "rgba(103, 194, 58,1)",
        "rgba(144, 147, 153,1)",
        "rgba(230, 162, 60,1)",
        "rgba(245, 108, 108,1)"
      ],
      meterData: {},
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        segmentShowStroke: true,
        scales: {
          yAxes: [
            {
              stacked: true,
              display: true,
              labelString: "Power(w)",
              ticks: {
                autoSkip: true,
                suggestedMin: 0 // minimum will be 0, unless there is a lower value.
              }
            }
          ],
          xAxes: [
            {
              stacked: true,
              ticks: {
                autoSkip: true
              },
              labelString: "time"
            }
          ]
        }
      },
      test: 17
    };
  },
  async created() {
    await loadKragToken();
    this.allMeterAddresses = await getAllMeters();
  },
  methods: {
    addMeter(_meterAddress) {
      console.log("NEW");
      console.log(_meterAddress);
      let lables = [];
      let values = [];
      let tokens = [];
      this.$gun
        .get(_meterAddress)
        .map()
        .on(function(value, time) {
          console.log("GUN" + this.$data.test);
          lables.push(time);
          values.push(value.power);
          tokens.push(value.tokens);
        }).bind(this)
        ;
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
      console.log("UDATE");
    },
    handleClose(tag) {
      delete this.meterData[tag.name];
      this.tags.splice(this.tags.indexOf(tag), 1);
      this.selectedMeters.splice(this.tags.indexOf(tag), 1);
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
      this.inputMeter = "";
    },
    timeConverter(UNIX_timestamp, dataType) {
      var a = new Date(UNIX_timestamp);
      var months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
      ];
      var year = a.getFullYear();
      var month = months[a.getMonth()];
      var date = a.getDate();
      var hour = a.getHours();
      var min = a.getMinutes() < 10 ? "0" + a.getMinutes() : a.getMinutes();
      var sec = a.getSeconds() < 10 ? "0" + a.getSeconds() : a.getSeconds();
      if (dataType == "hour") {
        return hour + ":" + min + ":" + sec;
      }
      if (dataType == "day") {
        return month + "/" + date + " " + hour + ":" + min;
      }
      if (dataType == "month") {
        return date + "/" + month + " " + hour + ":" + min;
      }
      if (dataType == "year") {
        return year + "/" + month + "/" + date;
      }
    }
  },

  computed: {
    datacollection() {
      if (this.meterData == undefined) {
      }
      try {
        let number = 30;
        let timeStamps = [];
        if (this.chartMode == "Minute") {
          if (
            this.$data.meterData[Object.keys(this.$data.meterData)[0]].lables[0]
              .length > 30
          ) {
            number = 30;
          } else
            number = this.$data.meterData[Object.keys(this.$data.meterData)[0]]
              .lables[0].length;

          for (let unixTimeStamp of this.$data.meterData[
            Object.keys(this.$data.meterData)[0]
          ].lables[0].slice(
            Math.max(
              this.$data.meterData[Object.keys(this.$data.meterData)[0]]
                .lables[0].length - number,
              0
            )
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "hour"));
          }
        }
        // console.log(timeStamps);
        // if (this.chartMode == "Hour") {
        //   if (this.$data.meterData.lables[0].length > 1800) {
        //     number = 1800;
        //   } else number = number = this.$data.meterData.lables[0].length;
        //   for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
        //     Math.max(this.$data.meterData.lables[0].length - number, 0)
        //   )) {
        //     var date = new Date(unixTimeStamp * 1000);
        //     timeStamps.push(this.timeConverter(date, "hour"));
        //   }
        // }

        // if (this.chartMode == "Day") {
        //   if (this.$data.meterData.lables[0].length > 43200) {
        //     number = 43200;
        //   } else number = number = this.$data.meterData.lables[0].length;
        //   for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
        //     Math.max(this.$data.meterData.lables[0].length - number, 0)
        //   )) {
        //     var date = new Date(unixTimeStamp * 1000);
        //     timeStamps.push(this.timeConverter(date, "day"));
        //   }
        // }

        // if (this.chartMode == "Week") {
        //   if (this.$data.meterData.lables[0].length > 302400) {
        //     number = 302400;
        //   } else number = number = this.$data.meterData.lables[0].length;
        //   for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
        //     Math.max(this.$data.meterData.lables[0].length - number, 0)
        //   )) {
        //     var date = new Date(unixTimeStamp * 1000);
        //     timeStamps.push(this.timeConverter(date, "month"));
        //   }
        // }

        // if (this.chartMode == "Month") {
        //   if (this.$data.meterData.lables[0].length > 1296000) {
        //     number = 1296000;
        //   } else number = number = this.$data.meterData.lables[0].length;
        //   for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
        //     Math.max(this.$data.meterData.lables[0].length - number, 0)
        //   )) {
        //     var date = new Date(unixTimeStamp * 1000);
        //     timeStamps.push(this.timeConverter(date, "month"));
        //   }
        // }

        console.log("KEY POINT");
        let keys = Object.keys(this.$data.meterData);
        console.log(keys);
        let dataValues = { labels: timeStamps, datasets: [] };
        for (let i = 0; i < keys.length; i++) {
          console.log(this.meterData[keys[i]]);
          dataValues.datasets.push({
            label: keys[i] + " Power Consumption",
            data: this.meterData[keys[i]].values[0].slice(
              Math.max(this.meterData[keys[i]].values[0].length - number, 0)
            ),
            backgroundColor: this.backgroundColors[i],
            borderColor: this.borderColors[i],
            borderWidth: 2
          });
        }
        console.log("DATA");
        console.log(dataValues);
        return dataValues;

        return "a";
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
