using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace ProductsCategories.Models
{
    public class ViewModel
    {
        public Product Product {get; set;}
        public Category Category {get; set;}
        public Grouping ProductCategory {get; set;}
        public List<Product> allProducts {get; set;}
        public List<Category> allCategories {get; set;}
        public List<Grouping> allProductsCategories {get; set;}
    }
}