<template>
  <el-row style="margin-bottom: 30px">
    <el-col :span="24">
      <el-card>
        <el-row style="text-align: left;padding: 10px;font-size: 22px">
          <el-col :span="18">
            <span class="card-title">{{title}}</span>
          </el-col>
          <el-col :span="6">
            <el-button style="float: right" type="primary" @click="onClickAddNewRow">上传文件</el-button>
          </el-col>
        </el-row>
        <transition name="fade">
          <el-row v-if="showNewRowForm">
            <el-upload
              ref="upload"
              class="upload-demo"
              action="http://localhost:8000/api/uploadPdf"
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              :before-remove="beforeRemove"
              :on-success="onSubmitSuccess"
              multiple
              :limit="100"
              :on-exceed="handleExceed"
              :file-list="fileList">
              <el-button size="small" type="primary">上传文件</el-button>
              <div slot="tip" class="el-upload__tip">可选择多个文件批量上传</div>
            </el-upload>
          </el-row>
        </transition>
        <transition name="fade">
          <basic-table-edit-row-form v-if="showEditRowForm" :table-name="tableName" :pdfId="pdfId" :title="title+'-编辑行'" :key-type-list="keyTypeList" :key-value-list="keyValueList" :row-data="editRowData" @sendUpdateForm="onRowUpdate"></basic-table-edit-row-form>
        </transition>
        <el-table :data="tableData.filter(data => !searchWord || data.full_name.toLowerCase().includes(searchWord.toLowerCase()))"
                  border style="width: 100%;margin-top: 20px" v-if="startRender">
          <el-table-column
            v-for="(item,index) in Object.keys(keyValueList)"
            :prop="item"
            :label="keyValueList[item]"
            :show-overflow-tooltip=true>
            <template slot-scope="scope">
              <div v-if="keyTypeList[item]==='checkbox'">
                {{scope.row[item]=== false ? '否' : '是'}}
              </div>
              <div v-else>
                {{scope.row[item]}}
              </div>
            </template>
          </el-table-column>
          <el-table-column align="right">
            <template slot="header" slot-scope="scope">
              <el-input
                v-model="searchWord"
                size="mini"
                placeholder="输入关键字搜索">
              </el-input>
            </template>
            <template slot-scope="scope">
              <el-button type="danger" size="small" @click="onDeletePdf(scope.row)" style="margin-right: 20px">删除</el-button>

              <el-radio name="editPdfId" v-model="editPdfId" :label="scope.row.pdf_id" @change="onClickRadio(scope.row)">编辑</el-radio>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>

  </el-row>
</template>

<script>
  import { deletePdf, getKeyValueList, getPdf } from '../../api/form'
  import BasicTableEditRowForm from '../../components/Form/BasicTableEditRowForm'
  import BasicTableNewRowForm from '../../components/Form/BasicTableNewRowForm'

  export default {
    name: 'PdfTable',
    components: { BasicTableEditRowForm, BasicTableNewRowForm },
    data() {
      return {
        title: 'PDF列表',
        pdfId: '',
        tableName: 'pdf_information',
        keyValueList: {},
        keyTypeList: {},
        tableData: [],
        startRender: false,
        showNewRowForm: false,
        showEditRowForm: false,
        editRowData: {},
        fileList: [],
        editPdfId: null,
        searchWord: ''

      }
    },
    mounted() {
      this.editPdfId = this.$store.state.app.editPdfId
      getKeyValueList(this.tableName).then(response => {
        let data = response.data
        if (data.code === 1) {
          this.keyTypeList = data.keyTypeList
          this.keyValueList = data.keyValueList
        } else {
          console.log('获取数据失败')
          console.log(response)
        }
      })
      this.initTableData()
    },
    methods: {
      onClickRadio(row) {
        this.$store.commit('setEditPdfId', row.pdf_id)
        this.$store.commit('setEditPdfName', row.full_name)

      },
      onClickAddNewRow() {
        this.showEditRowForm = false
        this.showNewRowForm = !this.showNewRowForm
      },

      //上传文档函数
      handleRemove(file, fileList) {
        console.log(file, fileList)
      },
      handlePreview(file) {
        console.log('x')
        console.log(file)
      },
      handleExceed(files, fileList) {
        this.$message.warning(`当前限制选择 100 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`)
      },
      beforeRemove(file, fileList) {
        return this.$confirm(`确定移除 ${file.name}？`)
      },
      onSubmitSuccess(response, file, fileList) {
        this.initTableData()
      },
      initTableData() {
        getPdf(this.pdfId, this.tableName).then(response => {
          let data = response.data
          if (data.code === 1) {
            this.tableData = data.tableData
            this.startRender = true
          } else {
            console.log('获取数据失败')
            console.log(response)
          }
        })
      },
      onDeletePdf(row) {
        this.$confirm('此操作将永久删除文件【' + row.full_name + '】的所有录入数据, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          deletePdf(row.pdf_id).then(response => {
            let res = response.data
            if (res.code === 1) {
              this.$message({
                message: '删除成功',
                type: 'success'
              })
              this.$store.commit('setEditPdfId', null)
              this.$store.commit('setEditPdfName', null)
              this.initTableData()
            }
          }).catch(exception => {
            console.log(exception)
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })

      }
    }
  }
</script>

<style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  {
    opacity: 0;
  }
</style>
