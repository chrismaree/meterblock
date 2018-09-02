<template>
  <div class="UsageChart">
    <h1 class="center">Meter Usage</h1>  


    <el-button @click="findMeter" type="primary">Find Meter</el-button>

              <el-radio-group v-model="chartMode">
      <el-radio-button label="Minute"></el-radio-button>
      <el-radio-button label="Hour"></el-radio-button>
      <el-radio-button label="Day"></el-radio-button>
      <el-radio-button label="Week"></el-radio-button>
    </el-radio-group>
    <div>
      <br>  
  </div>

  <el-card class="box-card" shadow="always" >
    <Bar :options="chartOptions" :chart-data="datacollection" style="hight:800px !important"></Bar>
  </el-card>    
  </div>
</template>

 <script>
import Bar from "./BarChart.js";
import store from "../store";

import {
  loadKragToken,
  getMetersToOwner
} from "../../utils/KraGTokenInterface";

export default {
  name: "UsageChart",
  props: {
    selectedMeter: String
  },
  components: {
    Bar
  },
  data() {
    return {
      metersToOwner: [],
      chartMode: "Hour",
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        segmentShowStroke: true,
        scales: {
          yAxes: [
            {
              display: true,
              labelString: "Power(w)",
              ticks: {
                autoSkip: true,
                suggestedMin: 0, // minimum will be 0, unless there is a lower value.
                suggestedMax: 0
              }
            }
          ],
          xAxes: [
            {
              ticks: {
                autoSkip: true
              },
              labelString: "time"
            }
          ]
        }
      },
      meterData: {
        lables: [],
        values: [],
        tokens: []
      }
    };
  },
  methods: {
    async findMeter() {
      await this.$gun
        .get(this.selectedMeter)
        .map()
        .on((value, time) => {
          console.log(this.selectedMeter);
          this.$data.meterData.lables.push(time);
          this.$data.meterData.values.push(value.power);
          this.$data.meterData.tokens.push(value.tokens);
        });
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
      try {
        let number;
        let timeStamps = [];
        if (this.chartMode == "Minute") {
          if (this.$data.meterData.lables.length > 30) {
            number = 30;
          } else number = number = this.$data.meterData.lables.length;

          for (let unixTimeStamp of this.$data.meterData.lables.slice(
            Math.max(this.$data.meterData.lables.length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "hour"));
          }
        }

        if (this.chartMode == "Hour") {
          if (this.$data.meterData.lables.length > 1800) {
            number = 1800;
          } else number = number = this.$data.meterData.lables.length;
          for (let unixTimeStamp of this.$data.meterData.lables.slice(
            Math.max(this.$data.meterData.lables.length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "hour"));
          }
        }

        if (this.chartMode == "Day") {
          if (this.$data.meterData.lables.length > 43200) {
            number = 43200;
          } else number = number = this.$data.meterData.lables.length;
          for (let unixTimeStamp of this.$data.meterData.lables.slice(
            Math.max(this.$data.meterData.lables.length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "day"));
          }
        }

        if (this.chartMode == "Week") {
          if (this.$data.meterData.lables.length > 302400) {
            number = 302400;
          } else number = number = this.$data.meterData.lables.length;
          for (let unixTimeStamp of this.$data.meterData.lables.slice(
            Math.max(this.$data.meterData.lables.length - number, 0)
          )) {
            var date = new Date(unixTimeStamp * 1000);
            timeStamps.push(this.timeConverter(date, "month"));
          }
        }

        if (this.chartMode == "Month") {
          if (this.$data.meterData.lables.length > 1296000) {
            number = 1296000;
          } else number = number = this.$data.meterData.lables.length;
          for (let unixTimeStamp of this.$data.meterData.lables.slice(
            Math.max(this.$data.meterData.lables.length - number, 0)
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
              data: this.$data.meterData.values.slice(
                Math.max(this.$data.meterData.lables.length - number, 0)
              ),
              backgroundColor: "rgba(64, 158, 255,0.2)",
              borderColor: "rgba(64, 158, 255,1)",
              borderWidth: 2
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