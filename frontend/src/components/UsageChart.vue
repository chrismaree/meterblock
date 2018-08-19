<template>
  <div class="UsageChart">
    <p>Enter the Meter Public key<p/>
    <input v-model="meterKey" name="key" class="input">
    <br>    
    {{meterData}}
    <br>
    <br>
    {{chartData}}
    <br>
    <el-button type="submit" @click="findMeter" class="button is-primary is-fullwidth subtitle">Find Meter</el-button>
    <br>
    <el-button type="submit" @click="b2" class="button is-primary is-fullwidth subtitle">b2</el-button>
         <line-chart :chart-data="datacollection"></line-chart>
    

  </div>
</template>

 <script>
// import Bar from './ReactiveBar.js'
import LineChart from "./LineChart.js";
// import Bar from 'vue-chartjs'
import store from "../store";

export default {
  name: "UsageChart",
  components: {
    LineChart
  },

  data() {
    return {
      // datacollection: null,
      chartData: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
        ],
        datasets: [
          {
            label: "GitHub Commits",
            backgroundColor: "#f87979",
            data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
          }
        ]
      },

      chartOptions: {
        segmentShowStroke: false,
        scales: {
          yAxes: [
            {
              display: true,
              ticks: {
                suggestedMin: 0 // minimum will be 0, unless there is a lower value.
              }
            }
          ]
        }
      },
      meterData: {
        lables: [],
        values: [],
        tokens: []
      },
      meterKey: "",
      labels: [0, 1, 2, 3, 4],

      data: [0, 1, 2, 3, 4]
    };
  },
  methods: {
    b2() {
      this.datacollection = {
        labels: this.$data.meterData.lables[0],
        datasets: [
          {
            data: this.$data.meterData.values[0],
            backgroundColor: "#f87979"
          }
        ]
      };
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    },
    findMeter() {
      console.log(this.$data.meterData);
      let lables = [];
      let values = [];
      let tokens = [];
      this.$gun
        .get(this.$data.meterKey)
        .map()
        .on(function(value, time) {
          console.log({ time: time, value: value });
          lables.push(time);
          values.push(value.power);
          tokens.push(value.tokens);
          // this.$data.meterData.push({ time: time, value: value });
        });

      this.$data.meterData.lables.push(lables);
      this.$data.meterData.values.push(values);
      this.$data.meterData.tokens.push(tokens);

      this.datacollection = {
        labels: this.$data.meterData.lables[0],
        datasets: [
          {
            data: this.$data.meterData.values[0],
            backgroundColor: "#f87979"
          }
        ]
      };

      console.log(this.$data.meterData);
    }
  },
  computed: {
    datacollection() {
      try {
        return {
          labels: this.$data.meterData.lables[0],
          datasets: [
            {
              data: this.$data.meterData.values[0],
              backgroundColor: Array.apply(
                null,
                Array(this.$data.meterData.values[0].length)
              ).map(String.prototype.valueOf, "#1fc8db")
            }
          ]
        };
      } catch (e) {
        return null;
      }
    }
  }
};
</script>