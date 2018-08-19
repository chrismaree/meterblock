<template>
  <div class="UsageChart">
    <p>Enter the Meter Public key<p/>
    <input v-model="meterKey" name="key" class="input">
    <br>    
    {{meterData}}
    <br>
    <br>
    {{datacollection}}
    <br>
    <el-button type="submit" @click="findMeter" class="button is-primary is-fullwidth subtitle">Find Meter</el-button>
    
    <Bar :chart-data="datacollection"></Bar>
    
  </div>
</template>

 <script>
import Bar from "./BarChart.js";
import store from "../store";

export default {
  name: "UsageChart",
  components: {
    Bar
  },

  data() {
    return {
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
      meterKey: ""
    };
  },
  methods: {
    findMeter() {
      let lables = [];
      let values = [];
      let tokens = [];
      this.$gun
        .get(this.$data.meterKey)
        .map()
        .on(function(value, time) {
          lables.push(time);
          values.push(value.power);
          tokens.push(value.tokens);
        });
      this.$data.meterData.lables.push(lables);
      this.$data.meterData.values.push(values);
      this.$data.meterData.tokens.push(tokens);
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
              ).map(String.prototype.valueOf, "#7ea9d6")
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