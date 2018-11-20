<template>
    <div>
        <div class="search-wrapper">
            <label>Class Code:</label>
            <input type="text" v-model="search" placeholder="Search title.."/>
            <label>Class Type</label>
            <select v-model="online" value="all">
                <option value="all">All</option>
                <option value="online">Online</option>
                <option value="face to face">Face to Face</option>
                <option value="hybrid">Hybrid</option>
            </select>
        </div>
        <table>
            <!-- <span v-for="section in classes" :key="section"> -->
                <!-- eslint-disable-next-line -->
                <tr v-for="class_section in filterTable" v-if="class_section.index != 0">
                    <!-- {{class_section}} -->
                    <td>{{ class_section.SC }} {{ class_section.CN }}</td>
                    <td>{{ class_section.CT }}</td>
                    <td>{{ class_section.IM }}</td>
                    <td>{{ class_section.SEC }}</td>
                    <td v-if="class_section.CR">{{class_section.CR}}</td>
                    <td v-else>0</td>
                    <td>{{ class_section.IN }}</td>
                    <td><a :href="class_section.CRN[1]">{{ class_section.CRN[0] }}</a></td>
                    <td>{{class_section.DT.days}} {{class_section.DT.times[0]}} - {{class_section.DT.times[1]}}</td>
                </tr>
            <!-- </span> -->
        </table>
    </div>
</template>

<script>
let c = require('../../../Wi-Q18_19.json')
let tmp = []

c.forEach(o => {
  o.collegeSubcategories.forEach(cat => {
      cat.classes.forEach(cl => {
        if (cl.index !== 0) { tmp.push(cl) }
      })
  })
})

const classes = tmp

function matchCourse (value, search) {
  if (search.length === 0) {
    return true
  }
  search = search.trim()
  let searchNumeric = search.toLowerCase().replace(/[abcdefghijklmnopqrstuvwxyz ]/g, '')
  let searchAlphabetic = search.toLowerCase().replace(/[1234567890 ]/g, '')

  return (
    (searchNumeric !== '' && searchAlphabetic !== '' && value.SC.toLowerCase().includes(searchAlphabetic) && value.CN.toLowerCase().includes(searchNumeric)) ||
      (value.SC.toLowerCase().includes(search.toLowerCase()) || value.CN.toLowerCase().includes(search.toLowerCase())) ||
      (search.toLowerCase().includes(value.SC.toLowerCase()) && search.toLowerCase().includes(value.CN.toLowerCase()))
  )
}
function matchIsOnline (value, search) {
  if (search === null || search.toLowerCase() === 'all') {
    return true
  }
  return value.IM.toLowerCase() === search.toLowerCase()
}
function filterBuilder (value, options) {
  return matchCourse(value, options.search) && matchIsOnline(value, options.online)
}

export default {
  name: 'DrexelTMS',
  data () {
    return {
      classes: null,
      search: '',
      online: 'all',
      maxIndex: 10
    }
  },
  created () {
    this.classes = classes
  },
  computed: {
    filterTable () {
      return this.classes.filter(value => {
        return filterBuilder(value, {
          search: this.search,
          online: this.online
        }
        )
      })
    }
  }
}
</script>

<style lang="scss" scoped>
table {

}
td {
    text-align: center;
    padding: 10px;
}
</style>
