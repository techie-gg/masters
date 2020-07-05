import React from 'react';
import ReactDOM from 'react-dom';

import {Button, Table,Modal, Form, Input, Select,message  } from 'antd';

import 'antd/dist/antd.css' 
import './App.css';


const { Option } = Select;

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};

const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

function handleErrors(response) {
  if (!response.ok) throw response;
  return response.json();
}


export default class App extends React.Component {
  formRef = React.createRef();

  constructor(props) {
    super(props);
  }

  state = {
    products : [],
    subCategories : [],
    categories : [],
    visible: false,
  }

  componentDidMount() {
      const apiUrl = 'http://127.0.0.1:8000/product_list/';
      fetch(apiUrl)
        .then(handleErrors)
        .then((data) => 
            this.setState({
              products: data
        })).catch((error) => {
          console.error(error); });

      const apiUrl2 = 'http://127.0.0.1:8000/sub_category_list/';
      fetch(apiUrl2)
        .then(handleErrors)
        .then((data) => 
            this.setState({
              subCategories: data
        })).catch((error) => {
          console.error(error); });

      const apiUrl3 = 'http://127.0.0.1:8000/category_list/';
      fetch(apiUrl3)
        .then(handleErrors)
        .then((data) => 
            this.setState({
              categories: data
         })).catch((error) => {
          console.error(error); });
          
  }

  showModal = () => {
    this.setState({
      visible: true,
    });
  };


  handleCancel = e => {
    this.setState({
      visible: false,
    });
  };

  handleSubmit = values => {
    this.setState({
      visible: false,
    });
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values)
    };
    fetch('http://127.0.0.1:8000/product_list/', requestOptions)
        .then(handleErrors)
        .then(data => 
          (this.setState({
            products: [data].concat(this.state.products)
          }),
          message.success("New Product Added Succesfully"))
          
          ).catch(error => {
            error.json().then((body) => {
              message.error(body.non_field_errors);
            });
          
          });
            
}

  
  render() {
    
    let { products,categories,subCategories } = this.state;

    let categoryFilter = [];
    let subCategoryFilter = [];
    let dropDownMix = [];


    if(categories){
      categories.map((item, key) =>
        categoryFilter.push(
          { text: item.name , value: item.name },
        ),
      );
    }

    if(subCategories){
     
      dropDownMix =  subCategories.map(item => <Option key={item.name +", " + item.category.name} value={item.id}>{item.name +", " + item.category.name}</Option>);


      subCategories.map((item, key) =>
        subCategoryFilter.push(
          { text: item.name , value: item.name },
        ),
      );
    }


    const columns = [{
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      sorter: (a, b) => { return a.name.localeCompare(b.name)},
      sortDirections: ['descend', 'ascend'],
    },  {
      title: 'Sub Category',
      render: (data) => data.sub_category.name,
      key: 'sub_category',
      filters: subCategoryFilter,
      onFilter: (value, record) => record.sub_category.name.includes(value),
      sorter: (a, b) => { return a.sub_category.name.localeCompare(b.sub_category.name)},
      sortDirections: ['descend', 'ascend'],
    },{
      title: 'Category',
      render: (data) => data.sub_category.category.name,
      key: 'category',
      filters: categoryFilter,
      onFilter: (value, record) => record.sub_category.category.name.includes(value),
      sorter: (a, b) => { return a.sub_category.category.name.localeCompare(b.sub_category.category.name)},
      sortDirections: ['descend', 'ascend'],
    }];
    return (
      <div>
        <div className="table-operations">
          <Button onClick={this.showModal}>Add</Button>
        </div>
        <Table columns={columns} dataSource={products} />
        <Modal
          title="Add Product"
          visible={this.state.visible}
          onCancel={this.handleCancel}
          footer={[]}
        >
         <Form {...layout} ref={this.formRef} name="control-ref" onFinish={this.handleSubmit} >
            <Form.Item  name="name" label="Product Name" rules={[{ required: true }]}>
              <Input />
            </Form.Item>
            <Form.Item name="sub_category" label="Sub Category" rules={[{ required: true }]}>
              <Select
                allowClear={true} showSearch placeholder="Sub Category"
                filterOption={(input, option) => option.props.key.toLowerCase().indexOf(input.toLowerCase()) >= 0}
              >
               {dropDownMix}
              </Select>
            </Form.Item>
            <Form.Item {...tailLayout}>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            
            </Form.Item>
            </Form>
        </Modal>
        
      </div>
    );
  }
}


ReactDOM.render(<App />, document.getElementById('root'));

