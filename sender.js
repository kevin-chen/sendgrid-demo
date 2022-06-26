require("dotenv").config();

const sgMail = require("@sendgrid/mail");
sgMail.setApiKey(process.env.SENDGRID_API_KEY);
console.log(process.env.SENDGRID_API_KEY);

console.log("Entering");

try {
  const msg = {
    to: "kevinchen3856@gmail.com",
    replyto: "contact@theheadstarter.com",
    from: {
      email: "contact@theheadstarter.com",
      name: "Helal Chowdhury",
    },
    templateId: process.env.TEMPLATE_ID,
    dynamicTemplateData: {
      squid_game_number: "001",
      first_name: "Kevin",
      last_name: "Chen",
    },
  };
  console.log("Preparing to Send");
  sgMail.send(msg);
  console.log("After SendGrid Send");
} catch (error) {
  console.log(error);
}
