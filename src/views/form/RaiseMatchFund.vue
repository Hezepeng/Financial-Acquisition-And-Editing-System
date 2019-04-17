<template>
  <div>
    <el-row id="area" :gutter="10" style="margin:30px 10px 10px 15px;">
      <el-col :span="11">
        <el-card :body-style="{ padding: '5px' }">
          <div style="padding: 5px">
            当前编辑的文件名：
            <span style="color: #409EFF">
            {{this.editPdfName}}
            </span>
          </div>
        </el-card>
        <div style="height: 10px"></div>
        <el-card :body-style="{ padding: '0px' }">
          <div v-show="showPdf">
            <div ref="pdfviewer" class="pdfobject-container"></div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="13" style="height:800px;overflow-y: scroll;" v-if="pdfId">
        <basic-table table-name="issuing_share_raising_matching_funds_basic_situation" :pdf-id="pdfId" title="募集配套资金-发行股份及募集配套资金基本概况"></basic-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import BasicForm from '../../components/Form/BasicForm'
  import BasicTable from '../../components/Form/BasicTable'
  import PDFObject from 'pdfobject'

  export default {
    name: 'RaiseMatchFund',
    components: { BasicTable, BasicForm },

    data() {
      return {
        screenHeight: document.documentElement.clientHeight,
        showPdf: true

      }
    },
    computed: {
      pdfId: function() {
        return this.$store.state.app.editPdfId
      },
      editPdfName: function() {
        return this.$store.state.app.editPdfName
      },
      documentOriginLocation: function() {
        return '/src/pdf/' + this.$store.state.app.editPdfName
      }

    },
    mounted() {
      if (!this.pdfId) {
        this.$alert('请先选择要编辑的文件', '温馨提示', {
          confirmButtonText: '去选择文件',
          center: true,
          callback: action => {
            this.$router.push({ name: 'pdfList' })
          }
        })
      }
    },
    watch: {
      toPage: {
        handler: function(val, oldVal) {
          this.$nextTick(function() {
            const pdfnode = this.$refs.pdfviewer
            // const pdfnodeleft = this.$refs.pdfviewerleft
            PDFObject.embed(this.documentOriginLocation, pdfnode, val)
            // PDFObject.embed(this.documentOriginLocation, pdfnodeleft, val)
          })
        },
        deep: true,
        immediate: true
      }
    }

  }
</script>

<style scoped>
  .pdfobject-container {
    height: 800px;
    width: 100%;
    display: block;
    margin: auto;
  }

  .pdfobject {
    border: 1px solid #666;
  }
</style>
