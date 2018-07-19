using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace ProductsCategories.Models
{
    public class Product
    {
        [Key]
        public int ProductId { get; set; }

        [Required(ErrorMessage = "A product name is required.")]
        [MinLength(2, ErrorMessage = "Product name must be more than 2 characters.")]
        public string Name { get; set; }

        [Required(ErrorMessage = "A description is required.")]
        public string Description { get; set; }

        [Required]
        public decimal Price { get; set; }
        public DateTime Created_At { get; set; }
        public DateTime Updated_At { get; set; }
        public List<Grouping> Categories {get; set;}
        public Product()
        {
            Created_At = DateTime.Now;
            Updated_At = DateTime.Now;
            Categories = new List<Grouping>();
        }
    }
}