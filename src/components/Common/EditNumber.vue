<template>
  <div style="padding: 10px">
    <el-input-number v-model="content" placeholder="请输入数字" :controls="false" :precision="2" :step="0.01" @blur="onValueChanged"></el-input-number>
  </div>

</template>

<script>
  import { saveSingleData } from '../../api/form'

  export default {
    name: 'EditNumber',
    props: {
      'type': {
        default: 'text'
      },
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
        content: '',
        inputType: 'text'
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
          this.$emit('sendInputChange', this.field, this.content)
        }

      }
    }
  }
</script>

<style scoped>

</style>
