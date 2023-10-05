<script>
const date = new Date();
const MOTHS = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
]
export default {
  data(){
    return {
      month: MOTHS[date.getMonth()],
      year: date.getFullYear(),
    }
  }
}
</script>

<template>
<div class="calendar-container">
  <div class="calendar__month">{{month}} {{year}}</div>

</div>
</template>

<style scoped>
.calendar-container {
  margin: 15px;
  width: 300px;
  height: 300px;
  border: 2px solid black;
  border-radius: 15px;
}
.calendar__month {
  text-align: center;
  padding: 10px 0;
  border-bottom: 1px solid black;
}
</style>