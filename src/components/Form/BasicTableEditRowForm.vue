<template>
  <el-row>
    <el-col :span="24">
      <el-card>
        <el-row style="text-align: left;padding: 10px;font-size: 22px">
          <span class="card-title">{{title}}</span>
        </el-row>
        <el-row v-for="(item,index) in Object.keys(keyValueList)" :key="item" v-if="startRender">
          <el-row style="text-align: left;padding: 15px 10px 0px 10px;font-size: 14px">
            <span v-if="keyTypeList[item]!=='checkbox'">{{keyValueList[item]}}</span>
          </el-row>
          <el-row>
            <edit-input v-if="keyTypeList[item]==='text'||keyTypeList[item]==='textarea'" :type="keyTypeList[item]" :name="item" :table-name="tableName" :pdf-id="pdfId" :field="item" :edit-content="form[item]" :auto-callback="true" @sendInputChange="onInputChange" :company-package-id="companyPackageId" :row-id="rowId"/>
            <edit-number v-else-if="keyTypeList[item]==='ratio'||keyTypeList[item]==='decimal'||keyTypeList[item]==='int'" :type="keyTypeList[item]" :pdfId="pdfId" :name="item" :table-name="tableName" :field="item" :edit-content="form[item]" :auto-callback="true" @sendInputChange="onInputChange" :company-package-id="companyPackageId" :row-id="rowId"/>
            <edit-checkbox v-else-if="keyTypeList[item]==='checkbox'" :label="keyValueList[item]" :name="item" :table-name="tableName" :field="item" :pdf-id="pdfId" :edit-content="form[item]" :auto-callback="true" @sendInputChange="onInputChange" :company-package-id="companyPackageId" :row-id="rowId"/>
            <edit-date-picker v-else-if="keyTypeList[item]==='datetime'" :pdfId="pdfId" :table-name="tableName" :field="item" :edit-content="form[item]" :auto-callback="true" @sendInputChange="onInputChange":company-package-id="companyPackageId" :row-id="rowId"/>
          </el-row>
        </el-row>
        <div style="margin-top: 10px;padding: 10px">
          <el-button type="primary" @click="onSaveTableRowData">关闭</el-button>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  import EditInput from '../Common/EditInput'
  import { getKeyValueList, getFormData, getTableRowData, saveTableRowData } from '../../api/form'
  import EditCheckbox from '../Common/EditCheckbox'
  import EditDatePicker from '../Common/EditDatePicker'
  import EditNumber from '../Common/EditNumber'

  export default {
    name: 'BasicTableEditRowForm',
    props: {
      'title': '',
      'tableName': '',
      'pdfId': '',
      'companyPackageId': {
        default: -1
      },
      rowData: {},
      keyValueList: {},
      keyTypeList: {}
    },
    data() {
      return {
        startRender: false,
        form: {},
        rowId: ''
      }
    },

    mounted() {
      this.form = this.rowData
      this.rowId = this.rowData.row_id
      this.startRender = true
      // getTableRowData(this.pdfId, this.tableName, this.rowId).then(response => {
      //   let data = response.data
      //   if (data.code === 1) {
      //     this.form = data.formData
      //     this.startRender = true
      //   } else {
      //     console.log('获取数据失败')
      //     console.log(response)
      //   }
      // })
    },
    methods: {
      onInputChange(field, content) {
        this.form[field] = content
      },
      onSaveTableRowData() {
        this.$emit('sendUpdateForm', this.form)
      },
      onCancel() {

      }
    },
    components: { EditNumber, EditDatePicker, EditCheckbox, EditInput }
  }
</script>

<style scoped>

</style>

