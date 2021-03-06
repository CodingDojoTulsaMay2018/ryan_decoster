using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Partials.Models
{
    public class LoginUser
    {
        [EmailAddress]
        [RegularExpression(@"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")]
        public string LogEmail { get; set; }

        [MinLength(8, ErrorMessage = "Password must be 8 or more characters.")]
        [DataType(DataType.Password)]
        public string LogPassword { get; set; }
    }

    public class RegisterUser
    {
        [Key]
        public int Id { get; set; }

        [Required(ErrorMessage = "First name field must not be empty.")]
        [RegularExpression("^[a-zA-Z]+$", ErrorMessage = "First name must be non-numerical.")]
        [MinLength(2)]
        [MaxLength(50)]
        public string First_Name { get; set; }

        [Required(ErrorMessage = "Last name field must not be empty.")]
        [RegularExpression("^[a-zA-Z]+$", ErrorMessage = "Last name must be non-numerical.")]
        [MinLength(2)]
        [MaxLength(50)]
        public string Last_Name { get; set; }

        [Required(ErrorMessage = "Email field must not be empty.")]
        [EmailAddress]
        [RegularExpression(@"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")]
        public string Email { get; set; }

        [Required(ErrorMessage = "Password field must not be empty.")]
        [MinLength(8, ErrorMessage = "Password must be 8 or more characters.")]
        [DataType(DataType.Password)]
        public string Password { get; set; }

        [Required(ErrorMessage = "Password confirm field must not be empty.")]
        [NotMapped]
        [Compare("Password", ErrorMessage = "Passwords do not match.")]
        public string Confirm { get; set; }
        public DateTime Created_At { get; set; }
        public DateTime Updated_At { get; set; }
    }
}