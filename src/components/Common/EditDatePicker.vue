<template>
  <div style="padding: 10px">
    <el-date-picker
      v-model="content"
      type="date"
      placeholder="选择日期"
      @blur="onValueChanged()"
      format="yyyy 年 MM 月 dd 日"
      value-format="yyyy-MM-dd">
    </el-date-picker>
  </div>
</template>

<script>
  import { saveSingleData } from '../../api/form'

  export default {
    name: 'EditDatePicker',
    props: {
      'editContent': {
        default: null
      },
      'field': '',
      'tableName': '',
      'pdfId': '',
      'rowId': '',
      'autoSave': {
        default: true
      },
      'autoCallback': {
        default: false
      },
      'companyPackageId': ''
    },
    data() {
      return {
        content: ''
      }
    },
    mounted() {
      this.content = this.editContent
    },
    methods: {
      onValueChanged() {
        if (this.autoSave) {
          saveSingleData(this.pdfId, this.tableName, this.rowId, this.field, this.content).then(response => {
            let res = response.data
            if (res.code === 1) {
              this.$message({
                message: '保存成功',
                type: 'success',
                duration: 1000,
                center: true
              })
              console.log(this.tableName + ' ' + this.field + ' ' + this.content, '自动保存成功')

            } else {
              this.$message.error({
                message: '保存失败',
                duration: 1000,
                center: true
              })
              console.log(this.tableName + ' ' + this.field + ' ' + this.content, '自动保存失败')
            }
          })
        }
        if (this.autoCallback) {
          console.log('callback')
          this.$emit('sendInputChange', this.field, this.content)
        }

      }
    }
  }
</script>

<style scoped>

</style>
