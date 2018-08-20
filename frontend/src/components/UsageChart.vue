<template>
  <div class="UsageChart">
    <el-row type="flex" justify="space-between">
      <el-col :span="10">
        <el-input placeholder="Meter Public key" v-model="meterKey"></el-input>
        </el-col>
      <el-col :span="4">
        <el-button type="submit" @click="findMeter" class="button is-primary is-fullwidth subtitle">Find Meter</el-button>
        </el-col>
      <el-col :span="10">
        <el-radio-group v-model="chartMode">
      <el-radio-button label="Minute"></el-radio-button>
      <el-radio-button label="Hour"></el-radio-button>
      <el-radio-button label="Day"></el-radio-button>
      <el-radio-button label="Week"></el-radio-button>
      <el-radio-button label="Month"></el-radio-button>
    </el-radio-group>
    </el-col>
    </el-row>
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

export default {
  name: "UsageChart",
  components: {
    Bar
  },

  data() {
    return {
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
                    autoSkip: false,
                suggestedMin: 0 // minimum will be 0, unless there is a lower value.
              }
            }
          ],
          xAxes: [
            {
              ticks: {
                    autoSkip: false,
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
        let number;
        if (this.chartMode == "Minute") {
          if (this.$data.meterData.lables[0].length > 30) {
            number = 30;
          } else number = number = this.$data.meterData.lables[0].length;
        }
        if (this.chartMode == "Hour") {
          if (this.$data.meterData.lables[0].length > 1800) {
            number = 1800;
          } else number = number = this.$data.meterData.lables[0].length;
        }
        if (this.chartMode == "Day") {
          if (this.$data.meterData.lables[0].length > 43200) {
            number = 43200;
          } else number = number = this.$data.meterData.lables[0].length;
        }
        let timeStamps = [];
        for (let unixTimeStamp of this.$data.meterData.lables[0].slice(
          Math.max(this.$data.meterData.lables[0].length - number, 0)
        )) {
          var date = new Date(unixTimeStamp * 1000);
          var hours = date.getHours();
          var minutes = "0" + date.getMinutes();
          var seconds = "0" + date.getSeconds();
          var formattedTime =
            hours + ":" + minutes.substr(-2) + ":" + seconds.substr(-2);
          timeStamps.push(formattedTime);
        }

        return {
          labels: timeStamps,
          datasets: [
            {
              label: this.meterKey + " Power Consumption",
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