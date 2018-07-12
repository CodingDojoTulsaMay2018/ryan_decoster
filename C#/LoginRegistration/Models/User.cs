using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace LoginRegistration.Models
{
    public class User
    {
        [Key]
        public long Id { get; set; }

        [Required]
        [MinLength(2)]
        [MaxLength(50)]
        public string First_Name { get; set; }

        [Required]
        [MinLength(2)]
        [MaxLength(50)]
        public string Last_Name { get; set; }

        [Required]
        [EmailAddress]
        [RegularExpression(@"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")]
        public string Email { get; set; }

        [Required]
        [MinLength(8)]
        [DataType(DataType.Password)]
        public string Password { get; set; }

        [Required]
        [NotMapped]
        [Compare("Password")]
        public string Confirm { get; set; }

        public DateTime Created_At { get; set; }
        public DateTime Updated_At { get; set; }
    }
}