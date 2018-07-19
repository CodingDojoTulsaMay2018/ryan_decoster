using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace ProductsCategories.Models
{
    public class Category
    {
        [Key]
        public int CategoryId { get; set; }

        [Required(ErrorMessage = "A category name is required.")]
        [MinLength(2, ErrorMessage = "Category name must be more than 2 characters.")]
        public string Name { get; set; }
        public List<Grouping> Products {get; set;}
        public DateTime Created_At { get; set; }
        public DateTime Updated_At { get; set; }
        
        public Category()
        {
            Created_At = DateTime.Now;
            Updated_At = DateTime.Now;
            Products = new List<Grouping>();
        }
    }
}